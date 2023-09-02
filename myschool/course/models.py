# course/models.py
from django.db import models
from user.models import Teacher

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    department = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.title
