from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostList.as_view()),
    # path('',views.index),
    # path('<int:pk>/',views.single_post_page),
    path("<int:pk>/", views.PostDetail.as_view()),
]
