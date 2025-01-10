from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .services import EmployeeService

# Create your views here.

# Tableau de board
def dashboard(request):

   context = {
      'title': 'Dashboard',
      'nb_employees': EmployeeService.count_employee()
   };

   return render(request, 'employee/dashboard.html', context)

# Liste des employés
def employee_list(request):
    employees = EmployeeService.get_all_employees()
    return render(request, 'employees/employee_list.html', {'employees': employees})

# Détails d'un employé
def employee_detail(request, pk):
    employee = EmployeeService.get_employee(pk)
    return render(request, 'employees/employee_detail.html', {'employee': employee})

# Création d'un nouvel employé
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            EmployeeService.create_employee(form)
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_form.html', {'form': form})

# Mise à jour d'un employé
def employee_update(request, pk):
    employee = EmployeeService.get_employee(pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            EmployeeService.update_employee(form)
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_form.html', {'form': form})

# Suppression d'un employé
def employee_delete(request, pk):
    employee = EmployeeService.get_employee(pk)
    if request.method == 'POST':
        EmployeeService.delete_employee(employee)
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})
