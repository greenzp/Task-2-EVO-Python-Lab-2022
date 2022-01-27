from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.FilteredListView.as_view(), name='all_users'),
    path('', views.say_hi, name='index'),
]
