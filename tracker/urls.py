from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

urlpatterns = [
    # Authentication URLs
    path('', lambda request: redirect('login')),
    path('login/', auth_views.LoginView.as_view(template_name='tracker/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    # Project Management URLs
    path('create/', views.create_project, name='create-project'),
    path('success/', views.success_page, name='project-success'),
    path('projects/', views.project_list, name='project-list'),
    path('projects/<int:project_id>/edit/', views.edit_project, name='edit-project'),
    path('projects/<int:project_id>/delete/', views.delete_project, name='delete-project'),
    # Messaging URLs
    path('send/', views.send_message, name='send-message'),
    path('message-success/', views.message_success, name='message-success'),
    path('inbox/', views.inbox, name='inbox'),
    path('messages/<int:message_id>/delete/', views.delete_message, name='delete-message'),
    # Password Reset URLs
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='tracker/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='tracker/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='tracker/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='tracker/password_reset_complete.html'), name='password_reset_complete'),
]