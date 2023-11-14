from django.core.validators import (MinLengthValidator)
from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=30, validators=[
                              MinLengthValidator(3)])
    
    def __str__(self) -> str:
        return self.title
    
    @classmethod
    def create(cls, title: str):
        if len(title) < 3:
            raise ValueError
        return cls.objects.create(title=title)