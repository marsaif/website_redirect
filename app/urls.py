from django.urls import path

from . import views

urlpatterns = [
    path("<str:job_id>/", views.redirect_to_url, name="redirect"),
    path("", views.welcome, name="welcome"),
]
