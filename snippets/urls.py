from django.urls import path
from . import views

urlpatterns = [
    path('', views.SnippetListView.as_view(), name='snippets-list'),
    path('<int:pk>/', views.SnippetDetailView.as_view(), name='snippets-detail')
]