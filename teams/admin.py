from django.contrib import admin

from teams.models import Team


class TeamAdmin(admin.ModelAdmin):
    model = Team
    
admin.site.register(Team, TeamAdmin)
