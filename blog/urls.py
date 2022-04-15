from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostList.as_view()),
    path("<int:pk>/", views.PostDetail.as_view()),
    path("category/<str:slug>", views.show_category_posts),
    path("tag/<str:slug>", views.show_tag_posts),
    path("create_post/", views.PostCreate.as_view()),
    path("update_post/<int:pk>/", views.PostUpdate.as_view()),
]
