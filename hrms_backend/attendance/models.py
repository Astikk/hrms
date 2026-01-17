from django.db import models
from employees.models import Employee

# Create your models here.
class Attendance(models.Model):
    PRESENT = 'P'
    ABSENT = 'A'

    STATUS_CHOICES = [
        (PRESENT, 'Present'),
        (ABSENT, 'Abset')
    ]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='attendance'
    )
    date = models.DateField()
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('employee', 'date')

    def __str__(self):
        return f"{self.employee.full_name} - {self.date}"
