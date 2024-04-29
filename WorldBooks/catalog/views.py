from .models import Book, Author, BookStatus, Genre
from django.http import HttpResponse


def index(request):
    return HttpResponse("Главная страница сайта Мир книг!!!!!!! str 334")


