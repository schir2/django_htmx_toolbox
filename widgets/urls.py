from django.urls import path
from .views import get_text, save_text

urlpatterns = [
    path('get_text/', get_text, name='get_text'),
    path('save_text/', save_text, name='save_text'),
]