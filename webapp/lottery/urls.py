# lottery/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('enter/', views.enter_lottery, name='enter_lottery'),
    path('results/', views.view_lottery_results, name='view_lottery_results'),
    # Add more URLs as needed
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
