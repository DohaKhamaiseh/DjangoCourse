from rest_framework import serializers
from watchlist_app.models import Watchlist, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    
    # we wrote this to convert the review_user(which in Review model) from intger field(FK) to string(user name)
    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        fields = "__all__"
        # we did this to avoid rewrites the watchlist id that we wanna create a review for it(th watchlist id is already in the url)
        # exclude = ('watchlist',)

class WatchlistSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)
    
    # overwrite platform field(which is an id refered to the platform) to be a name of that platform
    platform = serializers.CharField(source='platform.name')

    class Meta:
        model = Watchlist
        # __all__ to access all fields of the model
        fields = "__all__" 
        # fields = ['id', 'title', 'storyline','created'] 
        # the line above is equal to:
        # exclude = ['active']

class StreamPlatformSerializer(serializers.ModelSerializer):
    
    # if we use HyperlinkedModelSerializer instead of ModelSerializer each item wil known as url not id
    # the value of the name attribute in the streamplatform details should be like this : streamplatform-detail to work or I will get lookup-field error
    # ModelSerializer
    
    # this line use to show all watch list that hosted by each platform, so each platform may have more than one watch(movie)
    # watchlist this name should be the related_name that we added in the model
    # by using this we return all fields for each watch
    watchlist = WatchlistSerializer(many=True, read_only=True)
    
    # this will return what _str_ function return for each watch(movie)
    # watchlist = serializers.StringRelatedField(many=True)
    
    # this will return the id for each watch(movie)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    # this will return the link for each watch(movie) details(not actual one): "http://127.0.0.1:8000/watch/1/"
    # watchlist= serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     # view_name is the name that we added in the url of watch(movie) details
    #     view_name='watch-detail'
    # )
    
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"