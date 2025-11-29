from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectForm, MessageForm, RegisterForm
from .models import Project, Message
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

# Create your views here.
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse("Project created successfully!")
            return redirect('project-success')
    else:
        form = ProjectForm()
        
    return render(request, 'tracker/create_project.html', {'form': form})

def success_page(request):
    return render(request, 'tracker/success.html')

@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'tracker/project_list.html', {'projects': projects})


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('message-success')
    else:
        form = MessageForm()
    
    return render(request, 'tracker/send_message.html', {'form': form})

def message_success(request):
    return render(request, 'tracker/message_success.html')

def inbox(request):
    messages = Message.objects.filter(receiver=request.user, is_archived=False).order_by('-timestamp')
    return render(request, 'tracker/inbox.html', {'messages': messages})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Optional: log in user right after signup
            return redirect('inbox')  # Or redirect to 'inbox', etc.
    else:
        form = RegisterForm()
    
    return render(request, 'tracker/register.html', {'form': form})

def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project-list')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'tracker/edit_project.html', {'form': form, 'project': project})

@user_passes_test(lambda u: u.is_superuser)
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('project-list')


@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id, receiver=request.user)
    message.delete()
    return redirect('inbox')