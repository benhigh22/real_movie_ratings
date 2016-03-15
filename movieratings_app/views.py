import json

from django.forms import model_to_dict
from django.shortcuts import render
from movieratings_app.models import Movie, Review, Rater, NewReview
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse


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


def create_review(request):
    rating = request.POST.get('review')
    movie = request.POST.get('new_movie')
    if rating and movie:
        NewReview.objects.create(rating=rating, movie=movie)
        return HttpResponseRedirect(reverse('movieratings_app.views.create_review'))
    all_new_reviews = NewReview.objects.all()
    return render(request, "new_reviews.html", {
        "reviews": all_new_reviews
    })


def get_rater_view(request):
    if request.POST:
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        occupation = request.POST.get('occupation')
        zip_code = request.POST.get('zip_code')
        new_rater = Rater.objects.create(age=age, gender=gender, occupation=occupation,
                                         zip_code=zip_code)
        rater_dict = model_to_dict(new_rater)
        return HttpResponse(json.dumps(rater_dict), status=201, content_type="application/json")
    else:
        rater_list = list(Rater.objects.all().values())
        return HttpResponse(json.dumps(rater_list), content_type="application/json")


def get_single_rater(request, pk):
    single_rater = list(Rater.objects.filter(pk=pk).values())
    return HttpResponse(json.dumps(single_rater), content_type="application/json")


def get_movie_view(request):
    if request.POST:
        movie_title = request.POST.get('movie_title')
        release_date = request.POST.get('release_date')
        video_release_date = request.POST.get('video_release_date')
        imdb = request.POST.get('imdb')
        new_movie = Movie.objects.create(movie_title=movie_title, release_date=release_date,
                             video_release_date=video_release_date, imdb=imdb)
        movie_dict = model_to_dict(new_movie)
        return HttpResponse(json.dumps(movie_dict), status=201, content_type="application/json")
    else:
        movie_list = list(Movie.objects.all().values())
        return HttpResponse(json.dumps(movie_list), content_type="application/json")


def get_single_movie(request, pk):
    single_movie = list(Movie.objects.filter(pk=pk).values())
    return HttpResponse(json.dumps(single_movie), content_type="application/json")


def get_review_view(request):
    if request.POST:
        reviewer_id = request.POST.get('reviewer_id')
        movie_id = request.POST.get('movie_id')
        rating = request.POST.get('rating')
        new_rating = Review.objects.create(reviewer_id=reviewer_id, movie_id=movie_id, rating=rating)
        rating_dict = model_to_dict(new_rating)
        return HttpResponse(json.dumps(rating_dict), status=201, content_type="application/json")
    else:
        review_list = list(Review.objects.all().values())
        return HttpResponse(json.dumps(review_list), content_type="application/json")


def get_single_review(request, pk):
    single_review = list(Review.objects.filter(pk=pk).values())
    return HttpResponse(json.dumps(single_review), content_type="application/json")



