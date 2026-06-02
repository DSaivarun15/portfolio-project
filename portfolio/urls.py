from django.urls import path
from . import views

urlpatterns = [
    path('',views.projects_list, name='list_projects'),
    path('new/', views.create_project_view, name='create_project'),
]