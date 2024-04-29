from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Author, Book, Genre, Language, Status, BookStatus

admin.site.site_title = 'Мир Книги - Администратирование'  # Изменяем название Админки в header
admin.site.site_header = 'Мир Книги - Администратирование'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death', 'get_image')
    readonly_fields = ('get_image',)  # Добавляем изображение в "Редактирование книг панель администратора"

    def get_image(self, obj):   # Скрипт вывода изображения обложки книги в панели администратора
        return mark_safe(f'<img src="{obj.image.url}" width="80" height="100"')
    get_image.short_description = 'Изображение'


class BooksInstanceInline(admin.TabularInline):
    model = BookStatus


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_author', 'genre', 'language', 'get_image')
    readonly_fields = ('get_image',)  # Добавляем изображение в "Редактирование книг панель администратора"
    inlines = [BooksInstanceInline]

    def get_image(self, obj):   # Скрипт вывода изображения обложки книги в панели администратора
        return mark_safe(f'<img src="{obj.image.url}" width="80" height="100"')
    get_image.short_description = 'Изображение'


@admin.register(BookStatus)
class BookStatusAdmin(admin.ModelAdmin):
    list_display = ('book', 'status')
    fieldsets = (
        ('Экземпляр книги', {'fields': ('book', 'imprint', 'inv_now')
        }),
        ('Статус и окончание его действия', {'fields': ('status', 'due_back')
        }),
    )


admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)


