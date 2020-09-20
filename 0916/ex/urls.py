from django.urls import path
from . import views

urlpatterns = [
    path('', views.refresh, name = 'refresh'),
    path('profile_detail/<int:pk>', views.profile_detail, name = 'profile_detail'),
]
