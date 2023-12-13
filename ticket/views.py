# views.py
import pytz
from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth import get_user_model
from .form import CreateTicketForm , AssignTicketForm
from .models import Ticket
from project.models import Project,TeamLeader,Engineer
from accounts.models import User

User = get_user_model()

def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.user, request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.customer = request.user
            ticket.created_on = timezone.now()

            if ticket.project:
                ticket.manager = ticket.project.manager
                ticket.save()

                # Optionally, you can add more logic here

                messages.success(request, 'Ticket created successfully.')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Please select a valid project.')
                return redirect('create-ticket')
        else:
            messages.warning(request, 'Something went wrong. Please check form errors.')
            return redirect('create-ticket')
    else:
        form = CreateTicketForm(request.user)
        context = {'form': form}
        return render(request, 'ticket/create_ticket.html', context)
    
def assign_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, ticket_id=ticket_id)

    if request.method == 'POST':
        form = AssignTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            # You can add a success message here if needed
            return redirect('ticket-queue')
    else:
        form = AssignTicketForm(instance=ticket)

    return render(request, 'ticket/assign_ticket.html', {'form': form, 'ticket': ticket})

def ticket_details(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id=ticket_id) 
    context = {'ticket': ticket}
    return render(request, 'ticket/ticket_details.html', context)
        
#for cx viewing all active tickets
def customer_active_tickets(request):
    tickets = Ticket.objects.filter(customer = request.user , is_resolved = False).order_by('-created_on')
    context = {'tickets':tickets}
    return render(request , 'ticket/view_tickets.html' , context)

#for cx viewing all resolved tickets
def customer_resolved_tickets(request):
    tickets = Ticket.objects.filter(customer = request.user , is_resolved = True).order_by('-created_on')
    context = {'tickets':tickets}
    return render(request , 'ticket/view_tickets.html' , context)

def manager_view_tickets(request):
    managed_project_ids = request.user.managed_projects.values_list('id', flat=True)
    tickets = Ticket.objects.filter(project__id__in=managed_project_ids).order_by('-created_on')

    context = {'tickets': tickets}
    return render(request, 'ticket/view_tickets.html', context)

def admin_view_tickets(request):
    tickets = Ticket.objects.all().order_by('-created_on')
    context = {'tickets':tickets}
    return render(request , 'ticket/view_tickets.html' , context)

def team_leader_view_tickets(request):
    team_leader = TeamLeader.objects.get(user=request.user)
    tickets = Ticket.objects.filter(project=team_leader.project).order_by('-created_on')
    context = {'tickets': tickets}
    return render(request, 'ticket/view_tickets.html', context)

def engineer_view_tickets(request):
    tickets = Ticket.objects.filter(assigned_engineer = request.user).order_by('-created_on')
    context = {'tickets':tickets}
    return render(request , 'ticket/view_tickets.html' , context)

#For managers only
def ticket_queue(request):
    manager = request.user
    tickets = Ticket.objects.filter(manager=manager, assigned_engineer__isnull=True)

    context = {'tickets': tickets}
    return render(request, 'ticket/ticket_queue.html', context)

def submit_resolution(request, ticket_id):
    if request.method == 'POST':
        resolution_steps = request.POST.get('rs')
        try:
            ticket = Ticket.objects.get(ticket_id=ticket_id)
        except Ticket.DoesNotExist:
            messages.error(request, 'Ticket does not exist.')
            return redirect('engineer-view-tickets')

        # Check if the logged-in user is the assigned engineer
        if request.user == ticket.assigned_engineer:
            ticket.resolution_steps = resolution_steps
            ticket.save()
            messages.success(request, 'Resolution steps submitted successfully.')
            return redirect('engineer-view-tickets')
        else:
            messages.error(request, 'You are not authorized to submit resolution steps for this ticket.')
            return redirect('ticket-details', ticket_id=ticket_id)
    else:
        # Handle GET requests or other cases as needed
        return redirect('engineer-view-tickets')

def resolve_ticket(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id=ticket_id)

    # Check if the logged-in user is the customer and the ticket is not resolved
    if request.user == ticket.customer and not ticket.is_resolved:
        ticket.is_resolved = True
        ticket.save()
        messages.success(request, 'Ticket resolved successfully.')
        return redirect('ticket-details', ticket_id=ticket_id)
    else:
        messages.error(request, 'You are not authorized to resolve this ticket.')
        return redirect('ticket-details', ticket_id=ticket_id)










