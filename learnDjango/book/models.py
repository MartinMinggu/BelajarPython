from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    total_page = models.IntegerField()
    published_date = models.DateField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2 )
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.title
