from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('random/', views.random_page, name='random_page'),
    path('CSDN/', views.CSDN, name='CSDN'),
    path('GIT/', views.GIT, name='GIT'),
    path('search/', views.search, name='search'),

]