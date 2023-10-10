from rest_framework import serializers
from rest_framework import status
from watchlist_app.models import Movie

def len_name(value):
    """
     its a validators function, I can name it whatever I want
    """
    if len(value) < 3:
             # Note: I can't send a status message too: status=status.HTTP_406_NOT_ACCEPTABLE
            raise serializers.ValidationError("The Name: Short")

class MovieSerializer(serializers.Serializer):
    
    # read_only mean auto-increasing, not allow to edit
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[len_name])
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    def create(self,validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        # instance has the old data
        # validated_data has the new data
        instance.name = validated_data.get('name',instance.name)
        instance.description = validated_data.get('description',instance.description)
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        
        return instance
    
    # Notes: 
       # 1. If we have multiple validation(feild and object level) applied the priority is for feild-level validation
       # 2. If we have multiple validation(feild and validators level) applied the priority is for validators
    
    def validate_name(self, value):
        """
        a  feild-level validation function to check anything for a specific feild(from the model)
        the name of the function should be validate_the name of the feild, which is "name" here
        """
        # value : value of the name feild
        if len(value) < 3:
            # Note: I can't send a status message too: status=status.HTTP_406_NOT_ACCEPTABLE
            raise serializers.ValidationError("The Name is too Short")

        return value
    
    def validate(self,data):
         """
        a  object-level validation function to check anything for a specific object(one movie for example)
        the name of the function should be validate
        """
         # data is the values for all feilds for certain object(movie)
         if data['name'] == data['description']:
             raise serializers.ValidationError('The name and description of the movie can not be the same')
         
         return data
            