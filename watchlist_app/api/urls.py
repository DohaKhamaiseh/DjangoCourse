from django.urls import path, include
from rest_framework.routers import DefaultRouter

from watchlist_app.api.views import (WatchListAV, WatchDetailAV,
                                     StreamPlatformAV, StreamPlatformDetailAV,StreamPlatformVS,
                                     ReviewAV, ReviewDetailAV, ReviewCreateAV,
                                     ReviewUserAV,ReviewUserFilter,WatchListSearch, WatchListOrder)


# router = DefaultRouter()
# router.register('platform', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='watch-detail'),
    
    # this way of searching is uisng django-filter package
    # in the Postman we send it like this : 
      # http://127.0.0.1:8000/watch/list2/?search=netflix&The
      # http://127.0.0.1:8000/watch/list2/?search=netflix
      # http://127.0.0.1:8000/watch/list2/?search=The
    path('list2/', WatchListSearch.as_view(), name='watch-list'),
    
    
    # this way of Order is uisng django-filter package
       # in the Postman we send it like this : 
      # http://127.0.0.1:8000/watch/list2/?ordering=avg_rating   ---> Acending Order
      # http://127.0.0.1:8000/watch/list2/?ordering=-avg_rating   ---> Deacending Order(- before)
    path('list2/', WatchListOrder.as_view(), name='watch-list'),
    
    # path('',include(router.urls)),
    
    # what inside router doing the same of both these urls
     path('platforms/', StreamPlatformAV.as_view(), name='platform-list'),
    path('platform/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    
    #    path('reviews/', ReviewAV.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetailAV.as_view(), name='review-detail'),
    
    # to get all reviews to specific watch
     path('<int:pk>/reviews', ReviewAV.as_view(), name='review-list'),
     
     # to create a new review for a specific watch
       path('<int:pk>/review-create', ReviewCreateAV.as_view(), name='review-create'),
     
     # to get a specific review
    path('review/<int:pk>/', ReviewDetailAV.as_view(), name='review-detail'),
    
    # to get all reviews for a specific user by her/his username
    # this way of filtering called : Filtering against URL
    # in the Postman we send it like this : http://127.0.0.1:8000/watch/reviews/doha
    #  path('reviews/<str:username>/', ReviewUserAV.as_view(), name='user-reviews-detail'),
    
     # this way of filtering called : Filtering against query parameters
      # in the Postman we send it like this : http://127.0.0.1:8000/watch/reviews/?username=doha
    #  path('reviews/', ReviewUserAV.as_view(), name='user-reviews-detail'),
     
      # this way of filtering is uisng django-filter package
      # in the Postman we send it like this : 
      # http://127.0.0.1:8000/watch/reviews/?review_user__username=doha&active=true
      # http://127.0.0.1:8000/watch/reviews/?review_user__username=doha
      # http://127.0.0.1:8000/watch/reviews/?active=true
     path('reviews/', ReviewUserFilter.as_view(), name='user-reviews-detail'),
    
]