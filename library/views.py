from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Book
from django.http import HttpResponse

def get_books(request):
    if request.method == 'GET':
        books = list(Book.objects.all().values())
        return JsonResponse(books, safe=False)

@csrf_exempt  # Exempting CSRF protection for this view
def add_book(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        book = Book.objects.create(
            title=data['title'],
            author=data['author'],
            availability=True
        )
        return JsonResponse({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "availability": book.availability
        })

def home(request):
    return HttpResponse("Welcome to the Library Management System!")

