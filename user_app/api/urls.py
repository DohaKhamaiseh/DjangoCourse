from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user_app.api.views import registeration_view, logout_view

urlpatterns = [
    # Token:
    # this url to generate token by taking the username and password
    path('login/', obtain_auth_token, name='login'),
    
    # to add a new user
    path('register/', registeration_view, name='register'),
    
    # to logout the user
     path('logout/', logout_view, name='logout'),
     
     
     # JWT Authentication(You can use it or use normal Token(above)):
     # To generate an access(for 5 min.) token and refresh token(for 24 min.)
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # To generate an access token using refresh token after access expired
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
]