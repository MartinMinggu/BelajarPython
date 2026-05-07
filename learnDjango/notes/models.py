from django.db import models

# Create your models here.
class Note(models.Model):
    judul = models.CharField(max_length=100)
    konten = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Description(models.Model):
    deskripsi = models.CharField(max_length=100)
    kategori = models.TextField()
    def __str__(self):
        return self.deskripsi
# Note.objects.create(
#     judul="Belajar Django",
#     kontent="Hari ini belajar model"
# )


# Description.objects.create(
#     deskripsi="Belajar Django",
#     kategori="kategori1"
# )

