from django.db import models

# Create your models here.
class Product(models.Model):
    nama = models.CharField(max_length=200)
    deskrispi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nama