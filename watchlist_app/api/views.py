from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

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

class StreamPlatformVS(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving StreamPlatforms.
    """
    def list(self, request):
        """
        function to get list of objects from  StreamPlatform model
        """
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        function to retrieve a specific object from StreamPlatform model
        """
        queryset = StreamPlatform.objects.all()
        platform = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)
    
    def create(self,request):
        """
        function to create a new stream platform
        """
        serilalizer = StreamPlatformSerializer(data=request.data)
        if serilalizer.is_valid():
            serilalizer.save()
            
            # the status code here is by default 200 OK
            return Response(serilalizer.data)
        else:
            return Response(serilalizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        """
        function to update a specific stream platform(by id)
        """
        try:
             streamplatform = StreamPlatform.objects.get(pk = pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'Stream Platform Not Found'},status=status.HTTP_404_NOT_FOUND)
    
        serilalizer = StreamPlatformSerializer(streamplatform)
        if serilalizer.isvalid():
            serilalizer.save()
             # the status code here is by default 200 OK
            return Response(serilalizer.data)
        else:
            return Response(serilalizer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request,pk=None):
        """
        function to delete a specific stream platform(by id)
        """
        try:
             streamplatform = StreamPlatform.objects.get(pk = pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'stream platform Not Found'},status=status.HTTP_404_NOT_FOUND)
    
        streamplatform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
class ReviewAV(generics.ListAPIView):
    """
    view to get all reviews for a specific watch and not allowed to create one because we don't want to create a review for any watch from url that for specific watch
    """
    
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    # overwrite queryset function
    def get_queryset(self):
        # watchlist is the FKey in the Review model that represents the watch list
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
class ReviewCreateAV(generics.CreateAPIView):
    """
    View to create a new review for a given watch
    """
    
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    # overwrite queryset function
    def perform_create(self,serializer):
        """
        overwrite create function
        """
        # first watchlist is the watch that has this id(pk)
        # second watchlist is the FK in the Review model 
        pk = self.kwargs['pk']
        watchlist = Watchlist.objects.get(pk=pk)
        serializer.save(watchlist=watchlist)

class ReviewDetailAV(generics.RetrieveUpdateDestroyAPIView):
    """
    view to get, update and delete a specific review(by id)
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    

        