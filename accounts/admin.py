from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'get_full_name','email', 'get_role_display', 'get_enrolled_projects')

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Field Heading',
            {
                'fields': (
                    'is_customer',
                    'is_engineer',
                    'is_teamleader',
                    'is_manager',
                )
            }
        )
    )

    def get_role_display(self, obj):
        if obj.is_customer:
            return 'Customer'
        elif obj.is_engineer:
            return 'Engineer'
        elif obj.is_teamleader:
            return 'Team Leader'
        elif obj.is_manager:
            return 'Manager'
        elif obj.is_superuser:
            return 'Admin'
        
        return 'Unknown'

    get_role_display.short_description = 'Role'

    def get_enrolled_projects(self, obj):
        if obj.is_teamleader:
            projects = ', '.join([team_leader.project.project_title for team_leader in obj.teamleader_set.all()])
        elif obj.is_engineer:
            projects = ', '.join([engineer.team_leader.project.project_title for engineer in obj.engineer_set.all()])
        elif obj.is_customer:
            projects = ', '.join([project.project_title for project in obj.customer_projects.all()])
        elif obj.is_manager:
            projects = ', '.join([project.project_title for project in obj.managed_projects.all()])
        else:
            projects = 'None'

        return projects

    get_enrolled_projects.short_description = 'Enrolled Projects'

admin.site.register(User, CustomUserAdmin)

from django.contrib.auth.models import Group

class CustomGroupAdmin(admin.ModelAdmin):
    list_display = ('group_name_with_users',)

    def group_name_with_users(self, obj):
        return f"{obj.name} - {obj.user_set.count()} users"

    group_name_with_users.short_description = 'Group Name - Number of Users'

admin.site.unregister(Group)  # Unregister the default Group admin
admin.site.register(Group, CustomGroupAdmin)  # Register your custom Group admi