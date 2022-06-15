from django.urls import path, include
from . import views

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', views.create_users)
]