from django.urls import path
from . import views
from .views import register_new_employee
from .register_employee import *
from .register_site import *
from .register_team import *

from .list_attendance import *
from .list_employee import *
from .list_site import *
from .list_team import *

from .update_employee import *
from .update_site import *
from .update_team import *
app_name = 'employee'

urlpatterns = [
   path('dashboard/', views.dashboard, name='dashboard'),
   
   #urls pour enregistrer employés sites et equipes 
   path('register/employe', register_new_employee, name='register_employee'),
   path('register/site', register_new_site, name='register_new_site'),
   path('register/team', register_new_team, name='register_new_team'),
   
   #urls pour lister employés sites et equipes
   path('list/team', list_team, name='list_team'),
   path('list/site', list_site, name='list_site'),
   path('list/employee', list_employee, name='list_employee'),
   
   #urls pour lister les absences et présences
   path('list/attendance', list_attendance, name='list_attendance'),
   
   #urls pour modifier les informations d'employés sites et equipes
   path('update/employee', update_employee, name='update_employee'),
   path('update/site', update_site, name='update_site'),
   path('update/team', update_team, name='update_team'),
]
