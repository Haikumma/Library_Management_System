from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Book

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_books(request):
    books = list(Book.objects.all().values())
    return JsonResponse(books, safe=False)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_book(request):
    title = request.data.get('title')
    author = request.data.get('author')
    if not title or not author:
        return JsonResponse({'error': 'Title and author are required.'}, status=400)

    book = Book.objects.create(title=title, author=author, availability=True)
    return JsonResponse({'id': book.id, 'title': book.title, 'author': book.author, 'availability': book.availability})
