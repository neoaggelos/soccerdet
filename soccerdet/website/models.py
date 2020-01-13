from itertools import zip_longest
from django.db import models


class Person(models.Model):
    """A person"""

    def __str__(self):
        return self.full_name

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    description = models.CharField(max_length=300)
    quote = models.CharField(max_length=150)

    name = models.CharField(max_length=40)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Team(models.Model):
    """Team stats"""

    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    score = models.IntegerField()

    players = models.ManyToManyField(Person)

    @property
    def player_names(self):
        return [p.full_name for p in self.players.all()]


class Field(models.Model):
    """Stadium"""

    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)


class Match(models.Model):
    """Details for a single match"""

    def __str__(self):
        return f'{self.date} ({self.team_a} - {self.team_b})'

    date = models.DateField(auto_now=True)
    stadium = models.ForeignKey(Field, on_delete=models.CASCADE)

    team_a = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_a')
    team_b = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_b')

    def _team_attrs(self, this, other):
        if this.score > other.score:
            return 'text-success font-weight-bold'
        elif other.score > this.score:
            return 'text-danger'

        return ''

    @property
    def team_a_attrs(self):
        return self._team_attrs(self.team_a, self.team_b)

    @property
    def team_b_attrs(self):
        return self._team_attrs(self.team_b, self.team_a)

    @property
    def all_players(self):
        team_a_players = self.team_a.player_names
        team_b_players = self.team_b.player_names

        return zip_longest(team_a_players, team_b_players, fillvalue=Person(first_name='', last_name='', name=''))
