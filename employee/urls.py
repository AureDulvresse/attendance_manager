from django.urls import path
from . import views

app_name = 'employee'

urlpatterns = [
   path('dashboard/', views.dashboard, name='dashboard'),
   path('employee/list/', views.employee_list, name="list_employee"),
   path('employee/<int:pk>/', views.employee_detail, name='employee_detail'),
   path('employee/create/', views.employee_create, name='employee_create'),
   path('employee/<int:pk>/update/', views.employee_update, name='employee_update'),
   path('employee/<int:pk>/delete/', views.employee_delete, name='employee_delete'),
]
