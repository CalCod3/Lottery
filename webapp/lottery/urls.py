# lottery/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('enter/', views.enter_lottery, name='enter_lottery'),
    path('results/', views.view_lottery_results, name='view_lottery_results'),
    # Add more URLs as needed
]
