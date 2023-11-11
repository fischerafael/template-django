from django.core.validators import MinLengthValidator
from django.db import models

from brags.models.company.model import Company


class Category(models.Model):
    title = models.CharField(max_length=30, validators=[
                              MinLengthValidator(3)])
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True)
    
    def __str__(self) -> str:
        return self.title