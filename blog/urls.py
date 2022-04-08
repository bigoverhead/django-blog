from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostList.as_view()),
    path("<int:pk>/", views.PostDetail.as_view()),
    path("category/<str:slug>", views.show_category_posts),
]
