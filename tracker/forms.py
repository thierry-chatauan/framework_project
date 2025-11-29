from django import forms
from .models import Project, Message
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
    'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter project name'}),
    'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe the project','rows': 5,}),
    'start_date': forms.DateTimeInput(
        attrs={'class': 'form-control', 'type': 'datetime-local', 'placeholder': 'Start date and time'}
    ),
    'end_date': forms.DateTimeInput(
        attrs={'class': 'form-control', 'type': 'datetime-local', 'placeholder': 'End date and time'}
    ),
    'stakeholders': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'List stakeholders','rows': 5,}),
    'status': forms.Select(attrs={'class': 'form-control'}),
}

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'subject', 'body']
        widgets = {
            'receiver': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your message'}),
        }
        
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email',
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }