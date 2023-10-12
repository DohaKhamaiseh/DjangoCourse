from rest_framework import serializers
from watchlist_app.models import Watchlist, StreamPlatform

class WatchlistSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Watchlist
        # __all__ to access all fields of the model
        fields = "__all__" 
        # fields = ['id', 'title', 'storyline','created'] 
        # the line above is equal to:
        # exclude = ['active']

class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = "__all__"