from django.shortcuts import render
#  Custom import
from django.views import generic


# Create your views here.
class Home(generic.TemplateView):
    template_name = 'home.html'

