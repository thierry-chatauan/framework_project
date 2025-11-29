from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    STATUS_CHOICES = [
        ('IN', 'In Progress'),
        ('CO', 'Completed'),
        ('HO', 'On Hold'),
        ('CA', 'Canceled'),
    ]

    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    stakeholders = models.TextField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subject} (from {self.sender} to {self.receiver})"