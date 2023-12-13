from django.shortcuts import render , get_object_or_404
from .models import Project , TeamLeader , Engineer
from django.db.models import Case, When, Value
from ticket.models import Ticket

def project_details(request, project_id):
    project = Project.objects.get(project_id=project_id) 
    pending_tickets_count = Ticket.objects.filter(project=project, is_resolved=False).count()
    active_tickets_count = Ticket.objects.filter(project=project, is_resolved=True).count()

    context = {
        'project': project,
        'pending_tickets_count': pending_tickets_count,
        'active_tickets_count': active_tickets_count,
    }
    return render(request, 'project/project_details.html', context)

def customer_view_projects(request):
    projects = Project.objects.filter(customer=request.user).order_by(
    Case(
        When(status='Active', then=Value(0)),
        When(status='On Hold', then=Value(1)),
        When(status='Completed', then=Value(2)),
        default=Value(3),
    ),
    '-start_date'
)
    context = {'projects': projects}
    return render(request, 'project/view_projects.html', context)

def manager_view_projects(request):
    
    projects = Project.objects.filter(manager=request.user).order_by(
        Case(
            When(status='Completed', then=Value(0)),
            When(status='On Hold', then=Value(1)),
            default=Value(2),
        ),
        '-start_date'
    )
    context = {'projects': projects}
    return render(request, 'project/view_projects.html', context)

def team_leader_view_projects(request):
    # Assuming you have a way to get the TeamLeader instance
    team_leader = TeamLeader.objects.get(user=request.user)

    # Filtering projects based on the current team leader
    projects = Project.objects.filter(teamleader=team_leader).order_by(
        Case(
            When(status='Completed', then=Value(0)),
            When(status='On Hold', then=Value(1)),
            default=Value(2),
        ),
        '-start_date'
    )

    context = {'projects': projects}
    return render(request, 'project/view_projects.html', context)

def engineer_view_projects(request):
    engineer = Engineer.objects.get(user=request.user)

    projects = Project.objects.filter(teamleader__engineer=engineer).order_by('-start_date')

    context = {'projects': projects}
    return render(request, 'project/view_projects.html', context)

def admin_view_projects(request):
    projects = Project.objects.all().order_by(
    Case(
        When(status='Active', then=Value(0)),
        When(status='On Hold', then=Value(1)),
        When(status='Completed', then=Value(2)),
        default=Value(3),
    ),
    '-start_date'
)
    context = {'projects': projects}
    return render(request, 'project/view_projects.html', context)

def team_leader_view_engineers(request):
    team_leader = TeamLeader.objects.get(user=request.user)
    engineers = team_leader.engineer_set.all()
    
    context = {'engineers': engineers}
    return render(request, 'project/view_engineers.html', context)


def manager_view_team_members(request):
    # Assuming that the manager is associated with the project through the manager field
    manager_projects = Project.objects.filter(manager=request.user)

    # Retrieve team leaders and engineers for each project
    team_leader_data = []
    for project in manager_projects:
        team_leaders = TeamLeader.objects.filter(project=project)
        team_leader_info = [{'team_leader': team_leader, 'engineers': team_leader.engineer_set.all()} for team_leader in team_leaders]
        team_leader_data.append({'project': project, 'team_leaders_info': team_leader_info})

    context = {'team_leader_data': team_leader_data}
    return render(request, 'project/manager_view_team_members.html', context)

def admin_view_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, 'ticket/view_tickets.html', {'tickets': tickets})

def admin_view_ticket(request, project_id):
    project = get_object_or_404(Project, project_id=project_id)
    tickets = Ticket.objects.filter(project=project)
    return render(request, 'ticket/view_tickets.html', {'tickets': tickets})


    



   

