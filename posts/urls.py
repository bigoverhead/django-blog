from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.index, name="post"),
    path("<int:pk>/", views.detail, name="detail"),
]
