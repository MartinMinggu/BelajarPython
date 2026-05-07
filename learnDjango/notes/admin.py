from django.contrib import admin
from .models import Note, Description
# Register your models here.

# admin.site.register(Note)
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'judul','konten', 'created_at')
admin.site.register(Description)