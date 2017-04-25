from django.db import models


class Team(models.Model):
    ROUND_STATUS = (
            (1, 'Elimination round'),
            (2, 'Quarter-finals'),
            (3, 'Semi-finals'),
            (4, 'Final'),
            )
    name = models.CharField(max_length=50)
    round = models.PositiveSmallIntegerField(choices=ROUND_STATUS, default=1)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.name
