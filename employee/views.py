from django.shortcuts import render
from employee.services import EmployeeService

# Create your views here.
def dashboard(request):

   context = {
      'title': 'Dashboard',
      'nb_employees': EmployeeService.count_employee()
   };

   return render(request, 'employee/dashboard.html', context)