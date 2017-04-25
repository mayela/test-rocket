from django.db import models

from teams.models import Team


class Survey(models.Model):
    name = models.CharField(max_length=70)
    phone = models.CharField(max_length=12)
    favorite_team = models.ForeignKey(Team, related_name='surveys')
    ranking = models.PositiveSmallIntegerField()
    amount_bet = models.FloatField()
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Survey'
        verbose_name_plural = 'Surveys'

    def __str__(self):
        return "{} - {}".format(self.name, self.favorite_team.name)
