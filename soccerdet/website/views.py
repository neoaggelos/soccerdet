from django.shortcuts import render
from django.views.generic import TemplateView

from website.models import *

class HomeView(TemplateView):
    def get(self, request):
        return render(self.request, 'index.html', context={'lol': '123123'})

class PeopleView(TemplateView):
    def get(self, request):
        return render(self.request, 'people.html', context={
            'active': 'people',
            'all_people': Person.objects.all()
        })

class MatchesView(TemplateView):
    def get(self, request):
        matches = Match.objects.order_by('-date')
        return render(self.request, 'matches.html', context={
            'active': 'matches',
            'all_matches': enumerate(matches),
        })

class FieldsView(TemplateView):
    def get(self, request):
        matches = Match.objects.all()
        return render(self.request, 'fields.html', context={
            'active': 'fields',
            'all_fields': Field.objects.all()
        })
