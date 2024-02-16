from django.db import models
from django.contrib.auth.models import User


class TeamsList(models.Model):
    teams_choices = [
        ('arsenal', 'Arsenal'),
        ('aston_villa', 'Aston Villa'),
        ('bournemouth', 'Bournemouth'),
        ('brentford', 'Brentford'),
        ('brighton', 'Brighton'),
        ('burnley', 'Burnley'),
        ('chelsea', 'Chelsea'),
        ('crystal_palace', 'Crystal Palace'),
        ('everton', 'Everton'),
        ('fulham', 'Fulham'),
        ('liverpool', 'Liverpool'),
        ('luton_town', 'Luton Town'),
        ('man_city', 'Man City'),
        ('man_utd', 'Man Utd'),
        ('newcastle', 'Newcastle'),
        ('notts_forest', 'Notts Forest'),
        ('sheff_utd', 'Sheff Utd'),
        ('tottenham', 'Tottenham'),
        ('west Ham', 'West Ham'),
        ('wolves', 'Wolves'),
    ]
    team = models.CharField(max_length=40, choices=teams_choices, unique=True)

    def __str__(self):
        return self.team
