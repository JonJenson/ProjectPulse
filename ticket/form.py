# ticket/forms.py
from django import forms
from .models import Ticket
from project.models import Project  # Assuming your Project model is in the 'project' app
from accounts.models import User

class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['severity', 'ticket_title', 'ticket_description', 'project']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter projects for the current user (customer)
        self.fields['project'].queryset = Project.objects.filter(customer=user)

class AssignTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['assigned_engineer']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Filter the queryset to include only engineers
        self.fields['assigned_engineer'].queryset = User.objects.filter(is_engineer=True)