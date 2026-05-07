alur python django
python manage.py runserver : run server


python manage.py startapp product : buat app baru 
hasilnya ada dolder baru dengan nama produk


-- buat model nya di product/models.py
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

-- daftarkan di core/settings.py
-- bagian INSTALLED_APPS tamabhkan paling akhir  
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notes',
    'product',
    'student',
]


python manage.py makemigrations : buat migrations
python manage.py migrate : jalankan migrasi


table akan kebentuk di db


register di student/admin.py
from django.contrib import admin
from .models import Student
# Register your models here.
admin.site.register(Student) --auto ambil dari funtion __str__ di modelnya




run 
python manage.py runserver

akan muncul di 
http://127.0.0.1:8000/admin/