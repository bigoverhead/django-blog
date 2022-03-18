from django.views.generic import ListView, DetailView
from . import models


class PostList(ListView):

    model = models.Post
    context_object_name = "posts"
    template_name = "posts/post_list.html"


class PostDetail(DetailView):

    model = models.Post
    context_object_name = "post"
    template_name = "posts/post_detail.html"
