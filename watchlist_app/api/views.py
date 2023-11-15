from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


from watchlist_app.models import Watchlist, StreamPlatform, Review
from watchlist_app.api.serializers import (WatchlistSerializer, 
                                           StreamPlatformSerializer,
                                           ReviewSerializer)

from watchlist_app.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly
from watchlist_app.api.throttling import ReviewAVThrottle, ReviewCreateAVhrottle
from watchlist_app.api.pagination import WatchListPagination, WatchListLOPagintaion, WatchListCPagination

################ django-fliter package works with just views that inheritance from generics. ####################


class WatchListAV(generics.ListCreateAPIView):
    """
    View to get all Watchlist and create one
    """
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
    
    # The Admin is just who can create Watchlist
    permission_classes = [AdminOrReadOnly]
    # pagination_class = WatchListPagination
    # pagination_class = WatchListLOPagintaion
    # pagination_class = WatchListCPagination
    
class WatchDetailAV(generics.RetrieveUpdateDestroyAPIView):
    """
    View for get a specific Watchlist(by id) , update it and delete it
    """
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
    
    # The Admin is just who can edit Watchlists
    permission_classes = [AdminOrReadOnly]
   
           
class StreamPlatformAV(generics.ListCreateAPIView):
    
    """
    View to get all StreamPlatforms and create one
    """
    
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    
    #The Admin is just who can create Platform
    permission_classes = [AdminOrReadOnly]
      
class StreamPlatformDetailAV(generics.RetrieveUpdateDestroyAPIView):
    """
    View for get a specific StreamPlatform(by id) , update it and delete it
    """
    
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    
    #The Admin is just who can edit Platforms
    permission_classes = [AdminOrReadOnly]

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
    # this is object level permission, throttling(only the review list for specific watch will be restricted)
    # permission_classes= [IsAuthenticated]
    # here for Reviewlist requests by registered users we have 5 requests per day
    throttle_classes = [ReviewAVThrottle, AnonRateThrottle]
    
    
    
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
    # here for Review create requests by registered users we have 2 requests per day
    throttle_classes = [ReviewCreateAVhrottle]
    
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
        
        if watchlist.tot_rating ==0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
              watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating'])/2
              
        watchlist.tot_rating = watchlist.tot_rating+1
        watchlist.save()
        
        serializer.save(watchlist=watchlist,review_user=user)

class ReviewDetailAV(generics.RetrieveUpdateDestroyAPIView):
    """
    view to get, update and delete a specific review(by id)
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    # this is a custom permission
    permission_classes = [ReviewUserOrReadOnly]
    
    # permission_classes= [IsAuthenticated]
    
    # This is a scope throttling( don't need throttling.py file)
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'review-detail'
    

class ReviewUserAV(generics.ListAPIView):
    """
    A view to get all reviews for a user filtered by his/her username
    """
    

    serializer_class = ReviewSerializer
    
    # overwrite queryset function
    
    # this way of filtering called : Filtering against URL
    # def get_queryset(self):
    #     # username this as what in the URL
    #     username = self.kwargs['username']
    #     # review_user is an id for user so from that id I got her/his username( FKey in the Review model)
    #     return Review.objects.filter(review_user__username=username)
    
    # this way of filtering called : Filtering against query parameters
    def get_queryset(self):
        # username this as what in the URL as a query parameter
        username = self.request.query_params.get('username', None)
        # review_user is an id for user so from that id I got her/his username( FKey in the Review model)
        return Review.objects.filter(review_user__username=username)


class ReviewUserFilter(generics.ListAPIView):
    """
    A view for filter Reviews using django-filter package
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    # the fields are from Review model(the fields are in or relationship(we can send just one of them or both))
    # Filter(must be the exact name to get a result)
    filterset_fields = ['review_user__username', 'active']

class WatchListSearch(generics.ListAPIView):
    """
    A view for search watchlist using django-filter package
    """
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
    filter_backends = [filters.SearchFilter]
    # the fields are from WatchList model(the fields are in or relationship(we can send just one of them or both))
     # Search(must be just include name to get a result)
     # platform isa FK in WatchList model so I got from the id of it the name of the platform
    search_fields = ['title', 'platform__name']
    

class WatchListOrder(generics.ListAPIView):
    """
    A view for order watchlist using django-filter package
    """
    
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
    filter_backends = [filters.OrderingFilter]
    # the fields are from WatchList model(the fields are in or relationship(we can send just one of them or both))
     # Order(by default ascending order)
    ordering_fields = ['avg_rating']