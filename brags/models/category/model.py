from django.core.validators import MinLengthValidator
from django.db import models

from brags.models.company.model import Company


class Category(models.Model):
    title = models.CharField(max_length=30, validators=[
                              MinLengthValidator(3)])
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True)
    
    def __str__(self) -> str:
        return self.title

    @classmethod
    def list_all(cls):
        return cls.objects.all()
    
    @classmethod
    def find_by_id(cls, id: int):
        try: 
            return cls.objects.get(id=id)
        except:
            return None