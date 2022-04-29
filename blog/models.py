import os
from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
from django.contrib.auth.models import User


class Tag(models.Model):

    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/tag/{self.tag}/"


class Category(models.Model):

    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/category/{self.slug}/"


class Post(models.Model):

    title = models.CharField(max_length=30)
    content = MarkdownxField()
    hook_msg = models.TextField(blank=True)
    head_image = models.ImageField(
        upload_to="blog/images/%Y/%m/%d/",
        blank=True,
    )
    attached_file = models.FileField(
        upload_to="blog/files/%Y/%m/%d/",
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        User, related_name="posts", on_delete=models.SET_NULL, null=True
    )
    category = models.ForeignKey(
        Category,
        related_name="posts",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        default="no-category",
    )
    tags = models.ManyToManyField(Tag, blank=True)

    # methods
    def __str__(self):
        return f"[{self.pk}][{self.title}] :: {self.author}"

    def get_absolute_url(self):
        return f"/blog/{self.pk}/"

    def get_file_name(self):
        return os.path.basename(self.attached_file.name)

    def get_content_markdown(self):
        return markdown(self.content)


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} - {self.content}"

    def get_absolute_url(self):
        return f"{self.post.get_absolute_url}#comment-{self.pk}"
