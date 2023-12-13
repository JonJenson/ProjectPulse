from django.db import models
from django.contrib.auth import get_user_model
import random

User = get_user_model()

def generate_random_project_id():
    return random.randint(100000, 999999)

class TeamLeader(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_teamleader': True})
    project = models.ForeignKey('Project', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.get_full_name()} - {self.project.project_title}'

class Engineer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_engineer': True})
    team_leader = models.ForeignKey('TeamLeader', on_delete=models.CASCADE)

class Project(models.Model):
    project_code = models.CharField(max_length=20, unique=True)
    project_title = models.CharField(max_length=50)
    description = models.TextField()

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='customer_projects',
        limit_choices_to={'is_customer': True}
    )

    manager = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='managed_projects',
        limit_choices_to={'is_manager': True}
    )

    status = models.CharField(
        max_length=20,
        choices=(
            ('Active', 'Active'),
            ('Completed', 'Completed'),
            ('On Hold', 'On Hold'),
        ),
        default='Active'
    )

    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    project_id = models.IntegerField(unique=True, default=generate_random_project_id)

    def __str__(self):
        return self.project_title
