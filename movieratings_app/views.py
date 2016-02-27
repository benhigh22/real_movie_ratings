import operator

from django.db.models import Avg
from django.shortcuts import render, get_list_or_404

# Create your views here.
from movieratings_app.models import Movie, Review


def index_view(request):
    return render(request, "index.html", {})


def top_twenty(request):
    top_twenty_list = []
    for item in Movie.objects.all():
        top_twenty_list.append((item.movie_title, item.avg_rating))
    top_20_sorted = sorted(top_twenty_list, key=lambda x: x[1], reverse=True)[:20]
    return render(request, 'top_twenty.html', {'toptwenty': top_20_sorted})



"""def movie_detail(request, pk):
    reviewers = get_list_or_404(Review, movie_id=pk)
    movie = Movie.objects.get(id=pk)
    average = Review.objects.filter(movie_id=pk).aggregate(Avg('rating'))
    return render(request, 'movie_detail.html', {
        'reviewers': reviewers,
        'average': average,
        'movie': movie})
"""

def every_movie_view(request):
    average_rating = []
    for item in Movie.objects.all():
       average_rating.append((item.movie_title, (Review.objects.filter(movie=item).aggregate(Avg('rating')))))
    movie_rating = []
    for item in average_rating:
       movie_rating.append((item[0], item[1]['rating__avg']))
    all_movies = sorted(movie_rating, key=lambda x: x[0])
    return render(request, 'everymovie.html', {'all_movies': all_movies})


