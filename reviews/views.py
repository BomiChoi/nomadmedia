from django.contrib import messages
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from . import models
from books.models import Book
from movies.models import Movie
from . import forms

def create_review(request, pk):
  kind = request.GET.get('kind')
  print(kind)
  if not request.user.is_authenticated:
    return redirect(reverse("users:login"))
  else:
    form = forms.CreateReviewForm(request.POST)
    if kind == "movie":
      movie = Movie.objects.get_or_none(pk=pk)
      if not movie:
        return redirect(reverse("core:home"))
      if form.is_valid():
        review = form.save()
        review.movie = movie
        review.created_by = request.user
        review.save()
        messages.success(request, "Movie reviewed")
      return redirect(reverse("movies:movie", kwargs={"pk": movie.pk}))
    elif kind == "book":
      book = Book.objects.get_or_none(pk=pk)
      if not book:
        return redirect(reverse("core:home"))
      if form.is_valid():
        review = form.save()
        review.book = book
        review.created_by = request.user
        review.save()
        messages.success(request, "Book reviewed")
      return redirect(reverse("books:book", kwargs={"pk": book.pk}))


class DeleteReview(DeleteView):
  model = models.Review
  success_url = reverse_lazy("core:home")