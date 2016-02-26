import operator

from django.db.models import Avg
from django.shortcuts import render, get_list_or_404

# Create your views here.
from movieratings_app.models import Movie, Review


def index_view(request):
    return render(request, "index.html", {})


def get_average(request):
    average_rating = []
    for item in Movie.objects.all():
        average_rating.append(Review.objects.filter(movie=item).aggregate(Avg('rating')))
    top_twenty = sorted(average_rating, key=lambda k: k['rating__avg'], reverse=True)[:20]
    return render(request, "top_twenty.html", {'top_twenty': top_twenty})



"""
def get_stuff(request, pk):
    reviewers = get_list_or_404(Review, movie_id=pk)
    movie = Movie.objects.get(id=pk)
    average = Review.objects.filter(movie_id=pk).aggregate(Avg('rating'))
    return render(request, 'movie_detail.html', {
        'reviewers': reviewers,
        'average': average,
        'movie': movie})"""


