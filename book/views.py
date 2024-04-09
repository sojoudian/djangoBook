from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request, './templates/book_list.html',{'books':books})