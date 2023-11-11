from django.core.validators import MinLengthValidator
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=30,  validators=[
                              MinLengthValidator(3)])
    created_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.name}"
