from django.urls import path
from . import views

urlpatterns = [
    path('', views.snippet_list, name='snippets-list'),
    path('<int:id>/', views.snippet_detail, name='snippets-detail')
]