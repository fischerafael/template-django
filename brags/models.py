from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=30,  validators=[
                              MinLengthValidator(3)])
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.name}"


class Subscription(models.Model):
    title = models.CharField(max_length=30,  validators=[
                              MinLengthValidator(3)])
    monthly_price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)    

    def __str__(self):
        return f"{self.title} ($ {self.price})"


class CompanySubscription():
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    subscription = models.ForeignKey('Subscription', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateField(auto_now=True)