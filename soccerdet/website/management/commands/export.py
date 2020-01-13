import yaml

from django.core.management import BaseCommand
from website.models import *


class Command(BaseCommand):
    help = 'Export data to YAML'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            '--out', dest='output', default='soccerdet.yaml',
            help='Output YAML file.',
        )

    def handle(self, *args, **options):
        result = {
            'fields': [],
            'people': [],
            'matches': []
        }
        for field in Field.objects.all():
            result['fields'].append({
                'id': field.id,
                'name': field.name,
                'description': field.description,
                'image_url': field.image_url
            })

        for person in Person.objects.all():
            result['people'].append({
                'id': person.id,
                'name': person.name,
                'first_name': person.first_name,
                'last_name': person.last_name,
                'description': person.description,
                'quote': person.quote
            })

        for match in Match.objects.all():
            result['matches'].append({
                'id': match.id,
                'stadium': match.stadium.id,
                'date': match.date.strftime('%Y-%M-%d'),
                'team_a': {
                    'id': match.team_a.id,
                    'name': match.team_a.name,
                    'score': match.team_a.score,
                    'players': [player.id for player in match.team_a.players.all()]
                },
                'team_b': {
                    'id': match.team_b.id,
                    'name': match.team_b.name,
                    'score': match.team_b.score,
                    'players': [player.id for player in match.team_b.players.all()]
                },
            })

        with open(options.get('output'), 'w') as fout:
            yaml.dump(result, fout, allow_unicode=True)
