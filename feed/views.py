# from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, FormView

from .models import Post
from .forms import PostForm


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

    # Adding custom context data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Displaying dynamic Posts
        context['posts'] = Post.objects.all().order_by('-id')  # LIFO
        return context


# Render a "detail" view of an object.
class PostDetailView(DetailView):
    template_name = 'detail.html'
    model = Post


class AddPostForm(FormView):
    template_name = 'new_post.html'
    form_class = PostForm
    success_url = '/'   # index

    def form_valid(self, form):
        # create a new post
        new_object = Post.objects.create(
            text=form.cleaned_data['text'],
            image=form.cleaned_data['image'],
        )

        return super().form_valid(form)
