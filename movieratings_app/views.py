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
       average_rating.append((item.movie_title, (Review.objects.filter(movie=item).aggregate(Avg('rating')))))
   movie_n_rating = []
   for item in average_rating:
       movie_n_rating.append((item[0], item[1]['rating__avg']))
   print(movie_n_rating)
   top_twenty = sorted(movie_n_rating, key=operator.itemgetter(1), reverse=True)[:20]
   return render(request, 'top_twenty.html', {'toptwenty': top_twenty})