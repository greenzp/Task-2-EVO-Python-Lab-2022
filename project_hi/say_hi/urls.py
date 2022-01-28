from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.FilteredListView.as_view(), name='all_users'),
    path('', views.Say_Hi.as_view(), name='index'),
]
