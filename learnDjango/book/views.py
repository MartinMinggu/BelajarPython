from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.
def book_list(request):
    books   = Book.objects.all()
    text    = ""
    for book in books:
        text += book.title + "<br>"
    return HttpResponse(text)
