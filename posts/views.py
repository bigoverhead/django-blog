from django.shortcuts import render
from . import models


def index(request):

    posts = models.Post.objects.all().order_by("-pk")

    return render(request, "posts/index.html", context={"posts": posts})


def detail(request, pk):

    post = models.Post.objects.get(pk=pk)

    return render(request, "posts/detail.html", {"post": post})
