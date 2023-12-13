from django.contrib import admin
from .models import Project, TeamLeader, Engineer

class TeamLeaderInline(admin.TabularInline):
    model = TeamLeader

class EngineerInline(admin.StackedInline):
    model = Engineer

class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        TeamLeaderInline,
    ]

class TeamLeaderAdmin(admin.ModelAdmin):
    inlines = [
        EngineerInline,
    ]

admin.site.register(Project, ProjectAdmin)
admin.site.register(TeamLeader, TeamLeaderAdmin)
