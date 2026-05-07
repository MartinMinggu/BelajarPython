# Menampilkan View biasa 
# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Book
# # Create your views here.
# def book_list(request):
#     books   = Book.objects.all()
#     text    = ""
#     for book in books:
#         text += book.title + "<br>"
#     return HttpResponse(text)

# Menampilkan View berupa Html 
from django.shortcuts import render
from .models import Book
# Create your views here.
def book_list(request):
    books   = Book.objects.all()
    context = {
        'books' : books
    }
    return render(request, 'book_list.html', context)
