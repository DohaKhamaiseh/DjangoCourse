from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    
    # its a custom field 
    len_name = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        # __all__ to access all fields of the model
        fields = "__all__" 
        # fields = ['id', 'name', 'description'] 
        # the line above is equal to:
        # exclude = ['active']
        
    # we can add the validation functions here as it usual
    
    def get_len_name(self,object):
        """
        the name of the function should be get_the name of custom field
        object its refer to an object from Movie Model
        """
        return len(object.name)