from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    @property
    def number_of_departments(self):
        return self.department_set.count()

    @property
    def number_of_employees(self):
        return self.employee_set.count()
