from django.contrib.auth import get_user_model
from django.core.validators import (MaxValueValidator, MinLengthValidator,
                                    MinValueValidator)
from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=30, validators=[
                              MinLengthValidator(3)])
    
    def __str__(self) -> str:
        return self.title