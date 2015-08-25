# voting/models.py
from django.db import models

class Choice(models.Model):
    name = models.CharField(max_length=40, unique=True)
    votes = models.IntegerField(default=0)

# N.B. we don't use a Vote model as well because when querying the database,
# this requires a query involving the whole database (cross ChoiceXVote)