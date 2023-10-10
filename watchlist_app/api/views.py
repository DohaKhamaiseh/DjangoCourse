from rest_framework.response import Response
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework import status
from rest_framework.decorators import api_view

# if we didn't pass any parameters to api_view its by default "GET" view
@api_view(['GET', 'POST'])
def WatchListView(request):
    
    if request.method == 'GET':
        movies = Movie.objects.all()
        #  many=True to fetch all movies, we need to visit MovieSerializer many times
        serializer = MovieSerializer(movies,  many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
       serializer = MovieSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       else:
           return Response(serializer.errors)

@api_view(['GET', 'PUT','DELETE'])
def WatchDetailView(request,pk):
    
    if request.method == 'GET':
        # the try and except block is to check if the movie is in database or not
        try:
             movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Erorr':'Movie Not Found'},status=status.HTTP_404_NOT_FOUND)
       
        serializer = MovieSerializer(movie)
        # the status code here is by default 200 OK
        return Response(serializer.data)
    
    if request.method == 'PUT':
       # the try and except block is to check if the movie is in database or not
        try:
             movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Erorr':'Movie Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
           serializer.save()
           # the status code here is by default 200 OK
           return Response(serializer.data)
        else:
           return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
         # the try and except block is to check if the movie is in database or not
        try:
             movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Erorr':'Movie Not Found'},status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        #  return Response("The item deleted successfully")
        return Response(status=status.HTTP_204_NO_CONTENT)
    