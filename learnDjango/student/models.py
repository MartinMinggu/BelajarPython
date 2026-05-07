from django.db import models

# Create your models here.
class Student(models.Model):
    fisrt_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email    = models.EmailField(unique=True)
    age = models.IntegerField()
    birth_date = models.DateField()
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.fisrt_name} {self.last_name}"
