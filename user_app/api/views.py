from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from user_app.api.serializers import RegistrationSerializer
# this line to guarantee that the compiler will go to models.py to create the token
from user_app import models




@api_view(['POST'])
def registeration_view(request):
    
   if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            
            # all the lines before are enough just for creating user without his/her token, the lines after do it(creating token)
            data['Response'] = "Successfully created user"
            data['username'] = account.username
            data['email'] = account.email
            
            token = Token.objects.get(user=account).key
            
            data['token'] = token
        
        else:
            data = serializer.errors
            
        return Response(data)

@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        
        # by deleting the token we log out as a user and once we login again with same user we create a new token
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    
    