from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

from watchlist_app.models import Watchlist, StreamPlatform, Review
from watchlist_app.api.serializers import (WatchlistSerializer, 
                                           StreamPlatformSerializer,
                                           ReviewSerializer)


class WatchListAV(generics.ListCreateAPIView):
    """
    View to get all Watchlist and create one
    """
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
    
class WatchDetailAV(generics.RetrieveUpdateDestroyAPIView):
    """
    View for get a specific Watchlist(by id) , update it and delete it
    """
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
   
           
class StreamPlatformAV(generics.ListCreateAPIView):
    
    """
    View to get all StreamPlatforms and create one
    """
    
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
  
        
class StreamPlatformDetailAV(generics.RetrieveUpdateDestroyAPIView):
    """
    View for get a specific StreamPlatform(by id) , update it and delete it
    """
    
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

class ReviewAV(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    view to get all reviews for a specific watch and to create a new review
    """
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get(self, request, *args, **kwargs):
        """
        function to get all reviews for a specific watch
        """
        return self.list(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        """
        function to create a new review
        """
        return self.create(request, *args, **kwargs)

class ReviewDetailAV(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    view to get, update and delete a specific review(by id)
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get(self,request, *args, **kwargs):
        """
        function to get a specific review(by id)
        """
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        """ 
        function to update a specific review(by id)
        """
        return self.update(request, *args, **kwargs)
       
    def delete(self,request, *args, **kwargs):
        """
        function to delete a specific review(by id)
        """
        
        return self.destroy(request, *args, **kwargs)
        