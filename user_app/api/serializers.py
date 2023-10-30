from django.contrib.auth.models import User
from rest_framework import serializers


class RegistrationSerializer(serializers.ModelSerializer):
    
    # all other fields is from User model, we just create a new attribute which is pass2(confirm pass1)
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
       model = User
       fields=['username', 'email' , 'password','password2']
       
       # We add write_only to the built-in field password
       extra_kwargs = {
           'password'  :{'write_only' : 'True'}
       }
       
    def save(self):
        """
        override save method 
        """
        
        pass1 = self.validated_data['password']
        pass2 = self.validated_data['password2']
        
        if pass1 != pass2:
            raise serializers.ValidationError({'Error' : 'Pass1 and Pass2 must be the same'})
        
        # the DRF dosen't have resriction for same email (so I can add same email for different users) but we added it here
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'Error' : 'The email address already exists'})
        
        account = User.objects.create(username=self.validated_data['username'],email=self.validated_data['email'])
        # the password should be added like this to be encrypted
        account.set_password(self.validated_data['password'])
        account.save()
        
        return account
    
     