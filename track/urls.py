from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('tracker/', views.tracker, name='tracker'),
    path('nearby/', views.nearby, name='nearby'),
]
