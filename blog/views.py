from django.views.generic import ListView, DetailView
from . import models


class PostList(ListView):
    model = models.Post


class PostDetail(DetailView):
    model = models.Post
