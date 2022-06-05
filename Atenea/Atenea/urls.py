"""Atenea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('animalgames/', views.animalGames, name='animalGames'),
    path('numbergames/', views.numberGames, name='numberGames'),
    path('animal/games/whosthisanimalgame/', views.whosThisAnimalGame, name='whosThisAnimalGame'),
    # initial option
    path('numbergames/howmanynumbergame/', views.howManyNumberGame, name='howManyNumberGame'),
    path('numbergames/howmanynumbergamea/', views.howManyNumberGameA, name='howManyNumberGameA'),
    # urls for detection
    path('detect/', views.main, name='detect'),
]

urlpatterns += staticfiles_urlpatterns()
