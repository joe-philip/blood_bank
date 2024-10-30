from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.SignupAPIView.as_view()),
    path('blood_groups', views.BloodGroupsListAPIView.as_view())
]
