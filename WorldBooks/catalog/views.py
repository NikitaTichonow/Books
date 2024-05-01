from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View, generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import AuthorsForm


from .models import Book, Author, BookStatus, Genre
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound


def index(request):
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookStatus.objects.all().count()
    # Доступные книги (статус = 'На складе')
    num_instances_available = BookStatus.objects.filter(status__exact=2).count()
    num_authors = Author.objects.count()  # Метод 'all()' применен по умолчанию.

    # Количество посещений этого view, подсчитанное в переменной session
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Отрисовка HTML-шаблона index.html с данными внутри переменной context
    return render(request, 'index.html',
                  context={'num_books': num_books, 'num_instances': num_instances,
                           'num_instances_available': num_instances_available, 'num_authors': num_authors,
                           'num_visits': num_visits},
                  )

class BookListView(ListView):
    model = Book
    template_name = 'catalog/book_list.html'
    paginate_by = 2
    ordering = ['-id']


class BookDetailView(DetailView):
    model = Book
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        return render(request, "catalog/book_detail.html", {"book": book})


class AuthorListView(ListView):
    model = Author
    template_name = 'catalog/author_list.html'
    paginate_by = 2
    ordering = ['-id']


# получение данных из БД и загрузка шаблона authors_add.html
def authors_add(request):
    author = Author.objects.all()
    authorsform = AuthorsForm()
    return render(request, "catalog/authors_add.html", {"form": authorsform, "author": author})


# сохранение данных об авторах в БД
def create(request):
    if request.method == "POST":
        author = Author()
        author.first_name = request.POST.get("first_name")
        author.last_name = request.POST.get("last_name")
        author.date_of_birth = request.POST.get("date_of_birth")
        author.date_of_death = request.POST.get("date_of_death")
        author.save()
        return HttpResponseRedirect("/authors_add/")


# изменение данных в БД сохранение сведении об авторе
def edit(request, id):
        author = Author.objects.get(id=id)
        if request.method == "POST":
            author.first_name = request.POST.get("first_name")
            author.last_name = request.POST.get("last_name")
            author.date_of_birth = request.POST.get("date_of_birth")
            author.date_of_death = request.POST.get("date_of_death")
            author.save()
            return HttpResponseRedirect("/authors_add/")


# изменение данных в БД код для измененийй сведении об авторе
def edit1(request, id):
    author = Author.objects.get(id=id)
    if request.method == "POST":
        author.first_name = request.POST.get("first_name")
        author.last_name = request.POST.get("last_name")
        author.date_of_birth = request.POST.get("date_of_birth")
        author.date_of_death = request.POST.get("date_of_death")
        author.save()
        return HttpResponseRedirect("/authors_add/")
    else:
        return render(request, "edit1.html", {"author": author})


# удаление авторов из БД
def delete(request, id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect("/authors_add/")
    except Author.DoesNotExist:
        return HttpResponseNotFound("<h2>Автор не найден</h2>")


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Универсальный класс представления списка книг,
    находящихся в заказе у текущего пользователя.
    """
    model = BookStatus
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookStatus.objects.filter(borrower=self.request.user).filter(status__exact='2').order_by('due_back')


class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')


class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')








# def logout_view(request):
#     logout(request)
#     return redirect('') # на главную страницу сайта

# class AuthorListView(ListView):
#     model = Author
#
#     def get(self, request, pk):
#         author = Author.objects.get(id=pk)
#         return render(request, "catalog/book_detail.html", {"book": book})