from datetime import timedelta

from django.core.validators import (MaxValueValidator, MinLengthValidator,
                                    MinValueValidator)
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=30, validators=[
                              MinLengthValidator(3)])
    
    def __str__(self) -> str:
        return self.title
    
class Tag(models.Model):
    title = models.CharField(max_length=30, validators=[
                              MinLengthValidator(3)])
    
    def __str__(self) -> str:
        return self.title
    
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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    extra_link = models.URLField(blank=True, null=True)
    is_public = models.BooleanField(default=False)
    status = models.CharField(max_length=30, choices=STATUS)

    @property
    def tags(self):
        return self.bragtag_set.all()

    def __str__(self) -> str:
        return self.title
    

class BragTag(models.Model):
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
    brag = models.ForeignKey('Brag', on_delete=models.CASCADE)

    def __str__(self):
        return f"Tag: {self.tag.title} - Brag: {self.brag.title}"