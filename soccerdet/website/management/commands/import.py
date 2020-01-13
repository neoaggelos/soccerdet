import yaml
from datetime import datetime

from django.core.management import BaseCommand, CommandError
from website.models import *


class Command(BaseCommand):
    help = 'Export data to YAML'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            '--in', dest='input', default='soccerdet.yaml',
            help='Input YAML file.',
        )
        parser.add_argument(
            '--overwrite', dest='overwrite', default=False,
            help='Overwrite previous data', action='store_true'
        )

    def handle(self, *args, **options):
        overwrite = options.get('overwrite')

        try:
            data = yaml.safe_load(open(options.get('input')))

            Field.objects.all().delete()
            for field in data['fields']:
                Field(**field).save()

            Person.objects.all().delete()
            for person in data['people']:
                Person(**person).save()

            Team.objects.all().delete()
            Match.objects.all().delete()
            for match in data['matches']:
                team_a = Team(
                    id=match['team_a']['id'],
                    name=match['team_a']['name'],
                    score=match['team_a']['score']
                )
                team_a.save()
                for player_id in match['team_a']['players']:
                    team_a.players.add(Person.objects.get(id=player_id))
                team_a.save()

                team_b = Team(
                    id=match['team_b']['id'],
                    name=match['team_b']['name'],
                    score=match['team_b']['score']
                )
                team_b.save()
                for player_id in match['team_b']['players']:
                    team_b.players.add(Person.objects.get(id=player_id))
                team_b.save()

                Match(
                    id=match['id'],
                    date=datetime.strptime(match['date'], '%Y-%M-%d'),
                    stadium=Field.objects.get(id=match['stadium']),
                    team_a=team_a,
                    team_b=team_b
                ).save()

        except (yaml.YAMLError, KeyError, ValueError) as e:
            raise CommandError('invalid YAML file: ' + e)
