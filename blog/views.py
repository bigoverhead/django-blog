from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models


class PostList(ListView):

    model = models.Post
    ordering = "-pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = models.Category.objects.all()
        context["no_category_post_count"] = models.Post.objects.filter(
            category=None
        ).count()
        return context


class PostDetail(DetailView):

    model = models.Post


def show_category_posts(request, slug):

    category = models.Category.objects.get(slug=slug)

    context = {
        "categories": models.Category.objects.all(),
        "no_category_post_count": models.Post.objects.filter(
            category="no-category"
        ).count(),
        "category": category,
        "post_list": models.Post.objects.filter(category=category),
    }

    return render(request, "blog/post_list.html", context=context)
