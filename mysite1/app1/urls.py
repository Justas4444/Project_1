from django.urls import path

from . import views

urlpatterns = [
    path('predictions/', views.predictions_view, name='predictions'),
]