from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . import models


class PostUpdate(LoginRequiredMixin, UpdateView):

    model = models.Post
    fields = (
        "title",
        "content",
        "hook_msg",
        "head_image",
        "attached_file",
        "category",
    )

    def dispatch(self, request, *args, **kwargs):
        current_user = request.user
        if current_user.is_authenticated and current_user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionError


class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):

    model = models.Post
    fields = (
        "title",
        "content",
        "hook_msg",
        "head_image",
        "attached_file",
        "category",
    )

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (
            current_user.is_superuser or current_user.is_staff
        ):
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect("/")


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


def show_tag_posts(request, slug):

    tag = models.Category.objects.get(slug=slug)
    post_list = tag.post_set.all()

    context = {
        "categories": models.Category.objects.all(),
        "no_category_post_count": models.Post.objects.filter(
            category="no-category"
        ).count(),
        "post_list": post_list,
    }

    return render(request, "blog/post_list.html", context=context)
