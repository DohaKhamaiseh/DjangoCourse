from django.urls import path, include
from watchlist_app.api.views import (WatchListAV, WatchDetailAV,
                                     StreamPlatformAV, StreamPlatformDetailAV,
                                     ReviewAV, ReviewDetailAV, ReviewCreateAV)

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='watch-detail'),
    
     path('platforms/', StreamPlatformAV.as_view(), name='platform-list'),
    path('platform/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    
    #    path('reviews/', ReviewAV.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetailAV.as_view(), name='review-detail'),
    
    # to get all reviews to specific watch
     path('platform/<int:pk>/review', ReviewAV.as_view(), name='review-list'),
     
     # to create a new review for a specific watch
       path('platform/<int:pk>/review-create', ReviewCreateAV.as_view(), name='review-create'),
     
     # to get a specific review
    path('platform/review/<int:pk>/', ReviewDetailAV.as_view(), name='review-detail'),
    
]