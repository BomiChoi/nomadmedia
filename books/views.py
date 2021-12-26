from django.views.generic import ListView, DetailView, CreateView, UpdateView
from books.models import Book
from reviews import forms
from django.shortcuts import render


class BooksView(ListView):
  
  model = Book
  paginate_by = 15
  paginate_orphans = 5
  ordering = "-created_at"
  context_object_name = "books"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['page_title'] = "All Books"
    return context


class BookDetail(DetailView):
  model = Book
  context_object_name = 'book'

  def get(self, *args, **kwargs):
    pk = kwargs.get("pk")
    book = Book.objects.get_or_none(pk=pk)
    form = forms.CreateReviewForm()
    return render(
        self.request,
        "books/book_detail.html",
        {"book":book, "form": form},
    )



class CreateBook(CreateView):
  model = Book
  fields = (
    "title",
    "year",
    "cover_image",
    "rating",
    "category",
    "writer",
  )


class UpdateBook(UpdateView):
  model = Book
  fields = (
    "title",
    "year",
    "cover_image",
    "rating",
    "category",
    "writer",
  )