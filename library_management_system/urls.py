from django.contrib import admin
from django.urls import path
from library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # This will map the root URL
    path('books/', views.get_books, name='get_books'),
    path('books/add/', views.add_book, name='add_book'),
    path('api/books/', views.get_books, name='get_books'),  # Make sure this route is correct
    path('api/books/add/', views.add_book, name='add_book'),  # Add this route for adding books
    # other routes...
]
