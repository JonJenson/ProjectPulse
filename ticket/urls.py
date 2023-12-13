from django.urls import path 
from .import views

urlpatterns = [

path('create-ticket/', views.create_ticket, name='create-ticket'),
path('customer-active-tickets/', views.customer_active_tickets, name='customer-active-tickets'), 
path('customer-resolved-tickets/', views.customer_resolved_tickets, name='customer-resolved-tickets'), 
path('manager-view-tickets/', views.manager_view_tickets, name='manager-view-tickets'), 
path('admin-view-tickets/', views.admin_view_tickets, name='admin-view-tickets'), 
path('ticket-details/<int:ticket_id>', views.ticket_details, name='ticket-details'), 
path('ticket-queue', views.ticket_queue, name='ticket-queue'), 
path('assign-ticket/<int:ticket_id>', views.assign_ticket, name='assign-ticket'), 
path('team-leader-view-tickets', views.team_leader_view_tickets, name='team-leader-view-tickets'), 
path('engineer-view-tickets', views.engineer_view_tickets, name='engineer-view-tickets'), 
path('submit-resolution/<int:ticket_id>/', views.submit_resolution, name='submit-resolution'), 
path('resolve-ticket/<int:ticket_id>', views.resolve_ticket, name='resolve-ticket'), 


]