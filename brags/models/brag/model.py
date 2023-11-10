from datetime import timedelta

from django.contrib.auth import get_user_model
from django.core.validators import (MaxValueValidator, MinLengthValidator,
                                    MinValueValidator)
from django.db import models

from users.models import CustomUser

STATUS = [
    ("PENDING", "Pending"),
    ("IN-PROGRESS", "In Progress"),
    ("COMPLETED", "Completed"),
]

class Brag(models.Model):
    DEFAULT_DURATION = timedelta(hours=0.15)

    title = models.CharField(max_length=30,  validators=[
                              MinLengthValidator(3)])
    created_at = models.DateField(auto_now=True)
    duration = models.DurationField(default=DEFAULT_DURATION, validators=[
        MinValueValidator(timedelta(hours=0)),
        MaxValueValidator(timedelta(hours=24))  
    ])
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    extra_link = models.URLField(blank=True, null=True)
    is_public = models.BooleanField(default=False)
    status = models.CharField(max_length=30, choices=STATUS)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    @property
    def tags(self):
        return self.bragtag_set.all()

    def __str__(self) -> str:
        return self.title
    
    @classmethod
    def list_brags_by_user(cls, user):
        return cls.objects.filter(
            user = user
        )
    
    @classmethod
    def create(cls, title: str, user: CustomUser, duration: float = 0.15):
        cls.objects.create(
            title=title,
            user=user,
            duration=duration,
            status='PENDING'
        )