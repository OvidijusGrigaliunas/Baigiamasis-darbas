from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit_record', views.submit_record, name='submit_record'),
]