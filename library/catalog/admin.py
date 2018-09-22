from django.contrib import admin
from .models import Book, BookInstance, Author, Genre

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=('title','isbn', 'display_genre')
admin.site.register(Book, BookAdmin)

class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

admin.site.register(BookInstance, BookInstanceAdmin)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
admin.site.register(Author,AuthorAdmin)
admin.site.register(Genre)
