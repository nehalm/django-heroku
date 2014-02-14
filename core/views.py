
__author__ = 'file_author'

# Standard Library Imports

# Core Django Imports
from django.shortcuts import render
from django.views.generic import TemplateView

# Third Party Imports

# App Imports


class IndexTemplateView(TemplateView):
    template_name = 'index.html'

def error404(request):
    return render(request, '404.html')

def error500(request):
    return render(request, '500.html')