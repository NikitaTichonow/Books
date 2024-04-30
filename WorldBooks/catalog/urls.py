from django.urls import path
from .import views
from .views import BookListView, BookDetailView, AuthorListView


urlpatterns = [
    path('', views.index, name='index'),
    path('book_list/', BookListView.as_view(), name='books'),
    path('book_detail/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('author_list/', AuthorListView.as_view(), name='author'),
    path('authors_add/', views.authors_add, name='authors_add'),
    path('edit1/<int:id>/', views.edit1, name='edit1'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>/', views.delete, name='delete'),

]

urlpatterns += [
   path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
