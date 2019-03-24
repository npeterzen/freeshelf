from django import forms
from .models import Book

class SortForm(forms.Form):
    DISPLAY_CHOICES = [
        ('-added_on', 'Date Descending'),
        ('added_on', 'Date Ascending'),
        ('title', 'Title'),
    ]

    order = forms.ChoiceField(
        label="Sort by",
        choices = DISPLAY_CHOICES,
        required=False,
    )

    def sort(self):
        if not self.is_valid():
            return None
        
        data = self.cleaned_data
        
        books = Book.objects.all()
        if data['order']:
            books = books.order_by(data['order'])

        return books
