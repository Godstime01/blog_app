from django.urls import path
from .views import HomeListView, HomeDetailView

urlpatterns =[
    path('', HomeListView.as_view(), name = 'index'),
    path('post/<int:pk>/', HomeDetailView.as_view(), name='post-detail')
]