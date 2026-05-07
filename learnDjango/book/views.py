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



# rest api
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializer import BookSerializer


@api_view(['GET']) # hanya menerima get request
def book_api(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True) # convert banyak data menjadi JSON
    return Response(serializer.data)

@api_view(['GET']) # hanya menerima get request
def book_detail(request, id):
    try:
        books = Book.objects.get(id=id)
    except Book.DoesNotExist:
                return Response({'error': 'Book not found'}, status=404)
    serializer = BookSerializer(books) # convert banyak data menjadi JSON
    return Response(serializer.data)


@api_view(['POST'])
def book_create(request):
      serializer = BookSerializer(data=request.data)
      if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
      return Response(serializer.errors)

from .serializer import BookSerializer
from rest_framework.viewsets import ModelViewSet
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer