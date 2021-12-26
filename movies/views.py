from django.views.generic import ListView, DetailView, CreateView, UpdateView
from movies.models import Movie
from reviews import forms
from django.shortcuts import render


class MoviesView(ListView):

    model = Movie
    paginate_by = 15
    paginate_orphans = 5
    ordering = "-created_at"
    context_object_name = "movies"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "All Movies"
        return context


class MovieDetail(DetailView):
  model = Movie
  context_object_name = 'movie'
  def get(self, *args, **kwargs):
    pk = kwargs.get("pk")
    movie = Movie.objects.get_or_none(pk=pk)
    form = forms.CreateReviewForm()
    return render(
        self.request,
        "movies/movie_detail.html",
        {"movie":movie, "form": form},
    )


class CreateMovie(CreateView):
    model = Movie
    fields = (
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "director",
        "cast",
    )


class UpdateMovie(UpdateView):
    model = Movie
    fields = (
        "title",
        "year",
        "cover_image",
        "rating",
        "category",
        "director",
        "cast",
    )
