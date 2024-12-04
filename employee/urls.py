from django.urls import path
from . import views
from .views import register_new_employee

app_name = 'employee'

urlpatterns = [
   path('dashboard/', views.dashboard, name='dashboard'),
   path('register/', register_new_employee, name='register_employee'),
]
