from django.urls import path
from . import views

urlpatterns=[
    path('project-details/<int:project_id>/', views.project_details, name='project-details'),
    path('customer-view-projects/', views.customer_view_projects, name='customer-view-projects'), 
    path('manager-view-projects/', views.manager_view_projects, name='manager-view-projects'), 
    path('engineer-view-projects/', views.engineer_view_projects, name='engineer-view-projects'), 
    path('admin-view-projects/', views.admin_view_projects, name='admin-view-projects'), 
    path('team-leader-view-projects/', views.team_leader_view_projects, name='team-leader-view-projects'), 
    path('team-leader-view-engineers/', views.team_leader_view_engineers, name='team-leader-view-engineers'), 
    path('manager-view-team-members/', views.manager_view_team_members, name='manager-view-team-members'),
    path('admin-view-tickets',views.admin_view_tickets, name='admin-view-tickets'),
    path('admin-view-ticket/<int:project_id>/',views.admin_view_ticket, name='admin-view-ticket'),
  
]