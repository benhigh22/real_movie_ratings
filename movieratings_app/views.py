from django.shortcuts import render, get_list_or_404
from movieratings_app.models import Movie, Review, Rater


def index_view(request):
    return render(request, "index.html", {})


def top_twenty(request):
    top_twenty_sorted = Movie.objects.order_by('-avg_rating')[:20]
    return render(request, 'top_twenty.html', {'toptwenty': top_twenty_sorted})


def movie_detail(request, pk):
    users = Review.objects.filter(movie_id=pk)
    movie = Movie.objects.get(id=pk)
    return render(request, 'movie_detail.html', {'users': users, 'movie': movie})


def every_movie_view(request):
    every_movie = Movie.objects.all()
    return render(request, 'everymovie.html', {'movie': every_movie})


def every_user(request, pk):
    rater_info = Rater.objects.get(id=pk)
    rater_movie = Review.objects.filter(reviewer=rater_info.pk)
    return render(request, 'everyuser.html', {'rater': rater_info, 'rater_movie': rater_movie})

def each_movie(request, pk):
    movie_info = Movie.objects.get(id=pk)
    return render(request, 'each_movie.html',{'movie': movie_info})