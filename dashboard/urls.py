from django.urls import path
from . import views

urlpatterns = [
    path('', views.your_dashboard_view, name='dashboard_index'),

]
