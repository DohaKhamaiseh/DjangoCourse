from rest_framework.response import Response
from watchlist_app.models import Watchlist, StreamPlatform, Review
from watchlist_app.api.serializers import WatchlistSerializer, StreamPlatformSerializer, ReviewSerializer
from rest_framework import status
from rest_framework.views import APIView


class WatchListAV(APIView):
    """
    View to get all Watchlist and create one
    """
    def get(self,request):
        """
        function to get a list of Watchlist
        """
        watchlists = Watchlist.objects.all()
        serilalizer = WatchlistSerializer(watchlists, many=True)
        
         # the status code here is by default 200 OK
        return Response(serilalizer.data)
    
    def post(self,request):
        """
        function to create a new Watchlist
        """
        serilalizer = WatchlistSerializer(data=request.data)
        if serilalizer.is_valid():
            serilalizer.save()
            
            # the status code here is by default 200 OK
            return Response(serilalizer.data)
        else:
            return Response(serilalizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class WatchDetailAV(APIView):
    """
    View for get a specific Watchlist(by id) , update it and delete it
    """
    
    def get(self, request,pk):
        
        """
        function to get a specific Watchlist(by id)
        """
        try:
             watchlist = Watchlist.objects.get(pk = pk)
        except Watchlist.DoesNotExist:
            return Response({'Error':'Watchlist Not Found'},status=status.HTTP_404_NOT_FOUND)
       
        serilalizer = WatchlistSerializer(watchlist)
        
         # the status code here is by default 200 OK
        return Response(serilalizer.data)
    
    def put(self,request,pk):
        """
        function to update a specific Watchlist(by id)
        """
        try:
             watchlist = Watchlist.objects.get(pk = pk)
        except Watchlist.DoesNotExist:
            return Response({'Error':'Watchlist Not Found'},status=status.HTTP_404_NOT_FOUND)
    
        serilalizer = WatchlistSerializer(watchlist,data=request.data)
        if serilalizer.is_valid():
            serilalizer.save()
             # the status code here is by default 200 OK
            return Response(serilalizer.data)
        else:
            return Response(serilalizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        """
        function to delete a specific Watchlist(by id)
        """
        try:
             watchlist = Watchlist.objects.get(pk = pk)
        except Watchlist.DoesNotExist:
            return Response({'Error':'Watchlist Not Found'},status=status.HTTP_404_NOT_FOUND)
    
        watchlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
           
class StreamPlatformAV(APIView):
    
    """
    View to get all StreamPlatforms and create one
    """
    def get(self,request):
        """
        function to get a list of StreamPlatform
        """
        streamplatforms = StreamPlatform.objects.all()
         # context={'request': request} this is for HyperlinkedRelatedField in serializers.py and HyperlinkedModelSerializer
        serilalizer = StreamPlatformSerializer(streamplatforms, many=True, context={'request': request})
        
         # the status code here is by default 200 OK
        return Response(serilalizer.data)
    
    def post(self,request):
        """
        function to create a new StreamPlatform
        """
        serilalizer = StreamPlatformSerializer(data=request.data)
        if serilalizer.is_valid():
            serilalizer.save()
            
            # the status code here is by default 200 OK
            return Response(serilalizer.data)
        else:
            return Response(serilalizer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class StreamPlatformDetailAV(APIView):
    """
    View for get a specific StreamPlatform(by id) , update it and delete it
    """
    
    def get(self, request,pk):
        
        """
        function to get a specific StreamPlatform(by id)
        """
        try:
             streamplatform = StreamPlatform.objects.get(pk = pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'stream platform Not Found'},status=status.HTTP_404_NOT_FOUND)
       
        serilalizer = StreamPlatformSerializer(streamplatform)
        
         # the status code here is by default 200 OK
        return Response(serilalizer.data)
    
    def put(self,request,pk):
        """
        function to update a specific StreamPlatform(by id)
        """
        try:
             streamplatform = StreamPlatform.objects.get(pk = pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'stream platform Not Found'},status=status.HTTP_404_NOT_FOUND)
    
        serilalizer = StreamPlatformSerializer(streamplatform, data=request.data)
        if serilalizer.is_valid():
            serilalizer.save()
             # the status code here is by default 200 OK
            return Response(serilalizer.data)
        else:
            return Response(serilalizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        """
        function to delete a specific StreamPlatform(by id)
        """
        try:
             streamplatform = StreamPlatform.objects.get(pk = pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'Watchlist Not Found'},status=status.HTTP_404_NOT_FOUND)
    
        streamplatform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewAV(APIView):
    """
    view to get all reviews for a specific watch and to create a new review
    """
    
    def get(self,request):
        """
        function to get all reviews for a specific watch
        """
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
         # the status code here is by default 200 OK
        return Response(serializer.data)
    
    def post(self,request):
        """
        function to create a new review
        """
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
             # the status code here is by default 200 OK
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ReviewDetailAV(APIView):
    """
    view to get, update and delete a specific review(by id)
    """
    
    def get(self,requset,pk):
        """
        function to get a specific review(by id)
        """
        try :
            review = Review.objects.get(pk=pk)
        except review.DoesNotExist:
            return Response({'Error':'Review Not Found'},status=status.HTTP_404_NOT_FOUND)
           
        serializer = ReviewSerializer(review)
        
        # the status code here is by default 200 OK
        return Response(serializer.data)
    
    def put(self,request,pk):
        """ 
        function to update a specific review(by id)
        """
        try :
            review = Review.objects.get(pk=pk)
        except review.DoesNotExist:
            return Response({'Error':'Review Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            # the status code here is by default 200 OK
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        """
        function to delete a specific review(by id)
        """
        
        try:
            review = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response({'Error':'Review Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        