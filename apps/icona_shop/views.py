from django.shortcuts import render
from django.views.generic import TemplateView


class IconaPage(TemplateView):
    template_name = "index.html"
