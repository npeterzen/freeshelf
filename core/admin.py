from django.contrib import admin
from core.models import Book, BookCategory


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    exclude = ('slug',)


@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    