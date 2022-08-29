# from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

    # Adding custom context data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['greeting_message'] = "Hello to the world of Programming!"
        return context
