# from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

    # Adding custom context data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Displaying dynamic Posts
        context['posts'] = Post.objects.all()
        return context
