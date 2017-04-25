from django.contrib import admin

from surveys.models import Survey


class SurveyAdmin(admin.ModelAdmin):
    model = Survey
    fields = ('name', 'phone','favorite_team', 'ranking', 'amount_bet')

admin.site.register(Survey, SurveyAdmin)
