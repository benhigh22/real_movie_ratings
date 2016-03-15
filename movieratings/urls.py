"""movieratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from movieratings_app.views import index_view, top_twenty, every_movie_view, movie_detail, every_user, each_movie, \
    create_review, get_rater_view, get_movie_view, get_review_view, get_single_rater, get_single_movie, \
    get_single_review, post_movie

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view, name="index"),
    url(r'^toptwenty', top_twenty, name="top_twenty"),
    url(r'^(?P<pk>\d+)$', movie_detail, name="movie_detail"),
    url(r'^everymovie', every_movie_view, name="every_movie"),
    url(r'^user/(?P<pk>\d+)$', every_user, name="everyuser"),
    url(r'^movie/(?P<pk>\d+)$', each_movie, name="each_movie"),
    url(r'^newreviews', create_review, name="new_reviews"),
    url(r'^api/rater$', get_rater_view, name="get_rater"),
    url(r'^api/rater/(?P<pk>\d+)$', get_single_rater, name="get_single_rater"),
    url(r'^api/movie$', get_movie_view, name="get_movie"),
    url(r'^api/movie/(?P<pk>\d+)$', get_single_movie, name="get_single_movie"),
    url(r'^api/review$', get_review_view, name="get_review"),
    url(r'^api/review/(?P<pk>\d+)$', get_single_review, name="get_single_review"),
    url(r'^api/movie', post_movie, name="post_movie")
]
