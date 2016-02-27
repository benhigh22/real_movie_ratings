import operator

from django.db.models import Avg
from django.shortcuts import render, get_list_or_404

# Create your views here.
from movieratings_app.models import Movie, Review


def index_view(request):
    return render(request, "index.html", {})


def top_twenty(request):
    top_twenty_sorted = Movie.objects.order_by('-avg_rating')[:20]
    return render(request, 'top_twenty.html', {'toptwenty': top_twenty_sorted})


def movie_detail(request, pk):
    reviewers = get_list_or_404(Review, movie_id=pk)
    movie = Movie.objects.get(id=pk)
    average = Movie.objects.filter(id=pk)
    return render(request, 'movie_detail.html', {
        'reviewers': reviewers,
        'average': average,
        'movie': movie})


def every_movie_view(request):
    every_movie = Movie.objects.all()
    return render(request, 'everymovie.html', {'movie': every_movie})


