from django.shortcuts import render, get_object_or_404
from core.models import Book, BookCategory
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from core.forms import SortForm

def index_view(request):
    """View function for home page of site."""

    if request.GET:
        sortform = SortForm(request.GET)
        books = sortform.sort()
    else:
        sortform = SortForm()
        books = Book.objects.all()

    # book_list = Book.objects.all()
    categories = BookCategory.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(books, 10)

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    context = {
        'books': books,
        'categories': categories,
        'sort_form': sortform,
    }
    return render(request, 'core/index.html', context)

def book_detail_view(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'core/book_detail.html', {'book': book})

def category_detail_view(request, slug):
    category = get_object_or_404(BookCategory, slug=slug)
    return render(request, 'core/category_detail.html', {'category': category})


class BooksByCategoryDetailView(generic.DetailView):
    model = BookCategory
    template_name = 'core/books_by_category.html'
    context_object_name = 'category'
