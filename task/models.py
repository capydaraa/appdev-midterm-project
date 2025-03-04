from django.db import models
from django.utils import timezone


# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, editable=False, default='Pending') # Default value is 'Pending'

    def save(self, *args, **kwargs):
        if self.status != 'Completed':  # only updates the status if not completed
            if self.due_date < timezone.now().date(): # If due date is less than current date, then status is 'Overdue'
                self.status = 'Overdue'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title