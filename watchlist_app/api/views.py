from rest_framework.response import Response
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework import status
from rest_framework.views import APIView


class MovieListAV(APIView):
    """
    View to get all movies and create one
    """
    def get(self,request):
        """
        function to get a list of movies
        """
        movies = Movie.objects.all()
        serilalizer = MovieSerializer(movies, many=True)
        
         # the status code here is by default 200 OK
        return Response(serilalizer.data)
    
    def post(self,request):
        """
        function to create a new movie
        """
        serilalizer = MovieSerializer(data=request.data)
        if serilalizer.is_valid():
            serilalizer.save()
            
            # the status code here is by default 200 OK
            return Response(serilalizer.data)
        else:
            return Response(serilalizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class MovieDetailAV(APIView):
    """
    View for get a specific movie(by id) , update it and delete it
    """
    
    def get(self, request,pk):
        
        """
        function to get a specific movie(by id)
        """
        try:
             movie = Movie.objects.get(pk = pk)
        except Movie.DoesNotExist:
            return Response({'Error':'Movie Not Found'},status=status.HTTP_404_NOT_FOUND)
       
        serilalizer = MovieSerializer(movie)
        
         # the status code here is by default 200 OK
        return Response(serilalizer.data)
    
    def put(self,request,pk):
        """
        function to update a specific movie(by id)
        """
        try:
             movie = Movie.objects.get(pk = pk)
        except Movie.DoesNotExist:
            return Response({'Error':'Movie Not Found'},status=status.HTTP_404_NOT_FOUND)
    
        serilalizer = MovieSerializer(movie)
        if serilalizer.isvalid():
            serilalizer.save()
             # the status code here is by default 200 OK
            return Response(serilalizer.data)
        else:
            return Response(serilalizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        """
        function to delete a specific movie(by id)
        """
        try:
             movie = Movie.objects.get(pk = pk)
        except Movie.DoesNotExist:
            return Response({'Error':'Movie Not Found'},status=status.HTTP_404_NOT_FOUND)
    
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
           