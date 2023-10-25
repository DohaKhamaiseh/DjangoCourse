from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from watchlist_app.models import Watchlist, StreamPlatform, Review
from watchlist_app.api.serializers import (WatchlistSerializer, 
                                           StreamPlatformSerializer,
                                           ReviewSerializer)

from watchlist_app.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly


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

# class StreamPlatformVS(viewsets.ModelViewSet):
#     """
#     A simple ViewSet for viewing and editing stream platforms.
#     """
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer


class StreamPlatformVS(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for just viewing accounts.
    """
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer 
 
        
        
class ReviewAV(generics.ListAPIView):
    """
    view to get all reviews for a specific watch and not allowed to create one because we don't want to create a review for any watch from url that for specific watch
    """
    
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # this is object level permission


    
    
    # overwrite queryset function
    def get_queryset(self):
        # watchlist is the FKey in the Review model that represents the watch list
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
class ReviewCreateAV(generics.CreateAPIView):
    """
    View to create a new review for a given watch
    """
    
    
    serializer_class = ReviewSerializer
    
    # we need this for duplicating review issue
    def  get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self,serializer):
        """
        overwrite create function
        """
        # first watchlist is the watch that has this id(pk)
        # second watchlist is the FK in the Review model 
        pk = self.kwargs['pk']
        # from user line to if line is to prevent the user from duplicate the review
        user = self.request.user
        watchlist = Watchlist.objects.get(pk=pk)
        review_queryset =  Review.objects.filter(review_user=user, watchlist=watchlist)
        if review_queryset.exists():
            raise ValidationError("You already reviewed this watch!")
        serializer.save(watchlist=watchlist,review_user=user)

class ReviewDetailAV(generics.RetrieveUpdateDestroyAPIView):
    """
    view to get, update and delete a specific review(by id)
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    # this is a custom permission
    permission_classes = [ReviewUserOrReadOnly]
    

        