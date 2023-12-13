from django.db import models
from project.models import Project
import random
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

def random_ticket_id():
    return random.randint(100000, 999999)

class Ticket(models.Model):
    SEVERITY_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tickets')
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES, default='Low' )
    ticket_title = models.CharField(max_length=50)
    ticket_description = models.TextField()
    is_resolved = models.BooleanField(default=False)
    assigned_engineer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_tickets')
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_tickets')
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='manager_tickets')
    created_on = models.DateTimeField(default=timezone.now)
    ticket_id = models.IntegerField(unique=True , default=random_ticket_id)
    resolution_steps = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return f"{self.ticket_title} - #{self.ticket_id}"

