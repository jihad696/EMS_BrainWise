from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from company.models import Company
from department.models import Department

class Employee(models.Model):
    STATUS_CHOICES = (
        ('Hired', 'Hired'),
        ('Interview', 'Interview'),
        ('Rejected', 'Rejected'),
        ('Onboarding', 'Onboarding'),
    )

    # Basic Info
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile_number_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile_number = models.CharField(validators=[mobile_number_validator], max_length=17, blank=True)
    address = models.TextField(blank=True)
    designation = models.CharField(max_length=100)

    # Employment Info
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Interview')
    hired_on = models.DateField(null=True, blank=True)

    # Relationships
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.designation})"

    @property
    def days_employed(self):
        if self.hired_on and self.status == 'Hired':
            return (timezone.now().date() - self.hired_on).days
        return None

    def save(self, *args, **kwargs):
        # Business Logic: Ensure department belongs to the company
        if self.department.company != self.company:
            raise ValueError("The selected department does not belong to the selected company.")

        # Business Logic: Set hired_on date if status is 'Hired' and it's not set
        if self.status == 'Hired' and not self.hired_on:
            self.hired_on = timezone.now().date()

        super().save(*args, **kwargs)
