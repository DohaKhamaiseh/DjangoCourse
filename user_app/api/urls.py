from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import registeration_view, logout_view

urlpatterns = [
    # this url to generate token by taking the username and password
    path('login/', obtain_auth_token, name='login'),
    
    # to add a new user
    path('register/', registeration_view, name='register'),
    
    # to logout the user
     path('logout/', logout_view, name='logout'),

    
]