from django.urls import path
from library import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage for the library
    path('api/books/', views.get_books, name='get_books'),  # Fetch all books
    path('api/books/add/', views.add_book, name='add_book'),  # Add a new book
]