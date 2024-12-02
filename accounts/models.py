from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
class User(AbstractUser):

   class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

   def __str__(self):
        return self.name

   def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})

   def get_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip() if full_name.strip() else self.username
   
   def __str__(self):
        return self.get_full_name() or self.username
