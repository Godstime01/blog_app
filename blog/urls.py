from django.urls import path
from .views import (
    HomeListView,
    HomeDetailView,
    HomeCreateView,
    HomeUpdateView,
    HomeDeleteView,
)

urlpatterns = [
    path("", HomeListView.as_view(), name="index"),
    path("post/<int:pk>/", HomeDetailView.as_view(), name="post-detail"),
    path("post/new/", HomeCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/edit", HomeUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete", HomeDeleteView.as_view(), name="post_delete"),
]