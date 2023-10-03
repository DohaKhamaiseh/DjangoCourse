from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse

# Create your views here.


# function based view
# request is nessary to pass it even when I am not using it
def WatchListView(request):
    
    # to get all movies as a queryset
    movies = Movie.objects.all()
    
    # we should return JsonResponse and JsonResponse doesn't accept other than dictionary, so we convert the queryset to list then to dictionary
    data = {
        # values() to get all values for all attributes for all movies
        'movies':list(movies.values())
    }
    
    return JsonResponse(data)


def WatchDetailView(request, pk):
    movie = Movie.objects.get(pk = pk)
    data = {
        "name" : movie.name,
        "description": movie.description,
        "active": movie.active
    }
    
    return JsonResponse(data)