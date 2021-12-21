from django.contrib import admin

# Importing the models required
from books.models import Book

# registering the book file
admin.site.register(Book)