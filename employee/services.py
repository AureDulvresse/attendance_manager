from django.shortcuts import get_object_or_404
from .models import Employee

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
    
    @staticmethod
    def create_team(form):
        form.save()