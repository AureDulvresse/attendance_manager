from django.db import models
from django.conf import settings

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField()


class Team(models.Model):
    name = models.CharField(max_length=255)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="teams")


class Employee(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="employee_profile")
    
    # Informations personnelles
    gender = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')])
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=255)
    nationality = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=20, choices=[('celibatire', 'Célibataire'), ('marié', 'Marié(e)'), ('divorcé', 'Divorcé(e)'), ('widowed', 'Veuf/Veuve')])
    children_count = models.PositiveIntegerField(default=0)
    address = models.TextField()
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="employee_photos/", null=True, blank=True)

    # Informations professionnelles
    position = models.CharField(max_length=255)
    hire_date = models.DateField()
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=255)
    contract_type = models.CharField(max_length=20, choices=[('cdi', 'CDI'), ('cdd', 'CDD'), ('freelance', 'Freelance'), ('internship', 'Stage')])
    contract_duration = models.CharField(max_length=50, null=True, blank=True)
    contract_end_date = models.DateField(null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    supervisor = models.CharField(max_length=255, null=True, blank=True)

    # Informations familiales
    spouse_name = models.CharField(max_length=255, null=True, blank=True)
    spouse_profession = models.CharField(max_length=255, null=True, blank=True)
    emergency_contact = models.CharField(max_length=255)
    emergency_contact_relation = models.CharField(max_length=255)
    emergency_contact_phone = models.CharField(max_length=20)

    # Informations administratives
    resume = models.FileField(upload_to="resumes/", null=True, blank=True)
    degrees = models.TextField(null=True, blank=True)
    certifications = models.TextField(null=True, blank=True)
    social_security_number = models.CharField(max_length=50, null=True, blank=True)
    tax_status = models.CharField(max_length=50, null=True, blank=True)
    health_insurance = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.user.get_full_name() or self.user.username
