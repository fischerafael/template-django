from django.contrib.auth import get_user_model
from django.db import models

from brags.models.company.model import Company

ROLE = [
    ("CREATOR", "Creator"),
    ("ADMIN", "Admin"),
    ("USER", "User"),
]

class CompanyUser(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=ROLE)

    def __str__(self):
        return f"User: {self.user} - Company: {self.company}"