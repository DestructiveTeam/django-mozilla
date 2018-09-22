from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre(e.g. Science Fiction)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author',on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ','.join(genre.name for genre in self.genre.all()[:3])
    
    display_genre.short_description = 'Genre'

class BookInstance(models.Model):
    id = models.UUIDField(primary_key = True, default=uuid.uuid4, help_text='Unique ID for this particular book instance')
    book = models.ForeignKey('Book',on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    LOAN_STATUS=(
        ('m', 'Maintenace'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reseved'),
    )

    status = models.CharField(
        max_length = 1,
        choices = LOAN_STATUS,
        blank=True,
        default = 'm',
        help_text = 'Book availability',
    )

    class Meta:
        ordering = ['due_back']
    def __str__(self):
        return f'{self.id} ({self.book.title})'

