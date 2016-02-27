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

from movieratings_app.views import index_view, top_twenty

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view, name="index_view"),
    url(r'^toptwenty', top_twenty, name="top_twenty")
    #url(r'^moviedetail', movie_detail, name="movie_detail"),
    #url(r'^everymovie', every_movie_view, name="every_movie")
]
