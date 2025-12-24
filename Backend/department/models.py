from django.db import models
from company.models import Company

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.company.name})"

    @property
    def number_of_employees(self):
        return self.employee_set.count()
