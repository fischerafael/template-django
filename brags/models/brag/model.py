from datetime import timedelta

from django.contrib.auth import get_user_model
from django.core.validators import (MinLengthValidator)
from django.db import models
from brags.models.category.model import Category

from users.models import CustomUser

class Brag(models.Model):
    DEFAULT_DURATION = timedelta(hours=0.15)
    title = models.CharField(max_length=30,  validators=[
                              MinLengthValidator(3)])
    duration = models.DecimalField(max_digits=3, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=False)    
    created_at = models.DateField(auto_now=True)
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
    def create(cls, title: str, user: CustomUser, category: Category, duration: float = 0.15):       
        return cls.objects.create(
            title=title,
            user=user,
            duration=duration,
            is_public=False,
            category=category
        )
    
    @classmethod
    def find_by_id(cls, id: int):
        return cls.objects.get(id=id)
    
    @classmethod
    def add_tag(cls, brag_id: int, tag):       
        brag = cls.find_by_id(brag_id)
        print('**** brag id', brag)