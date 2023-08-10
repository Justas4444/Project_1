from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('predictions/', views.predictions_view, name='predictions'),
]