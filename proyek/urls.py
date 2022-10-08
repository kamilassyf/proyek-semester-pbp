from django.urls import path
from proyek.views import show_base

app_name = 'proyek'

urlpatterns = [
    path('', show_base, name='show_base'),
]