from django.shortcuts import get_object_or_404
from .models import Employee, Team

class EmployeeService:
      """Service dédié à la gestion des employés."""

      @staticmethod
      def get_all_employees():
        """Retourne tous les employés."""
        return Employee.objects.all()

      @staticmethod
      def get_employee(pk):
        """Retourne un employé spécifique."""
        return get_object_or_404(Employee, pk=pk)

      @staticmethod
      def create_employee(form):
        """Crée un nouvel employé à partir d'un formulaire valide."""
        form.save()

      @staticmethod
      def update_employee(form):
        """Met à jour un employé à partir d'un formulaire valide."""
        form.save()

      @staticmethod
      def delete_employee(employee):
        """Supprime un employé."""
        employee.delete()

      @staticmethod
      def count_employee(team=None):
        """
        Compte le nombre d'employés.

        Args:
            team (str, optional): Nom de l'équipe pour filtrer les employés. Si None, compte tous les employés.

        Returns:
            int: Nombre d'employés.
        """
        if team:
            return Employee.objects.filter(team=team).count()
        return Employee.objects.count()

      @staticmethod
      def search_employee(name=None, team=None, hire_date=None):
        """
        Rechercher des employés par nom, équipe et/ou date d'engagement.

        Args:
            name (str, optional): Nom ou partie du nom de l'employé à rechercher. Si None, pas de filtrage par nom.
            team (str, optional): Nom de l'équipe pour filtrer les employés. Si None, pas de filtrage par équipe.
            hire_date (date, optional): Date d'engagement. Si None, pas de filtrage par date.

        Returns:
            QuerySet: Liste des employés correspondant aux critères.
        """
        filters = {}
        if name:
            filters['name__icontains'] = name
        if team:
            filters['team'] = team
        if hire_date:
            filters['hire_date'] = hire_date
        
        return Employee.objects.filter(**filters)

class TeamService:
   """Service dédié à la gestion des équipes."""

   @staticmethod
   def get_all_teams():
     """Retourne toutes les équipes."""
     return Team.objects.all()

   @staticmethod
   def get_team(pk):
     """Retourne une équipe spécifique."""
     return get_object_or_404(Team, pk=pk)

   @staticmethod
   def get_employees_of_team(pk):
     """
     Retourne tous les employés d'une équipe spécifique.

     Args:
         pk (int): ID de l'équipe.

     Returns:
         QuerySet: Liste des employés de l'équipe.
     """
     team = get_object_or_404(Team, pk=pk)
     return team.employee_set.all()

   @staticmethod
   def create_team(form):
     """Crée une nouvelle équipe à partir d'un formulaire valide."""
     if form.is_valid():
         return form.save()
     raise ValueError("Le formulaire est invalide.")

   @staticmethod
   def update_team(form):
     """Met à jour une équipe à partir d'un formulaire valide."""
     if form.is_valid():
         return form.save()
     raise ValueError("Le formulaire est invalide.")

   @staticmethod
   def delete_team(pk):
     """
     Supprime une équipe spécifique.

     Args:
         pk (int): ID de l'équipe à supprimer.
     """
     team = get_object_or_404(Team, pk=pk)
     team.delete()

   @staticmethod
   def add_employee_to_team(team_pk, employee_pk):
     """
     Ajoute un employé à une équipe.

     Args:
         team_pk (int): ID de l'équipe.
         employee_pk (int): ID de l'employé à ajouter.

     Returns:
         Team: Équipe mise à jour.
     """
     team = get_object_or_404(Team, pk=team_pk)
     employee = get_object_or_404(Employee, pk=employee_pk)
     team.employee_set.add(employee)
     return team

   @staticmethod
   def remove_employee_from_team(team_pk, employee_pk):
     """
     Supprime un employé d'une équipe.

     Args:
         team_pk (int): ID de l'équipe.
         employee_pk (int): ID de l'employé à supprimer.

     Returns:
         Team: Équipe mise à jour.
     """
     team = get_object_or_404(Team, pk=team_pk)
     employee = get_object_or_404(Employee, pk=employee_pk)
     team.employee_set.remove(employee)
     return team

   @staticmethod
   def count_employees_in_team(pk):
     """
     Compte le nombre d'employés dans une équipe.

     Args:
         pk (int): ID de l'équipe.

     Returns:
         int: Nombre d'employés dans l'équipe.
     """
     team = get_object_or_404(Team, pk=pk)
     return team.employee_set.count()
