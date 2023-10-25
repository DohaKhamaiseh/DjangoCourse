from django.urls import path, include
from rest_framework.routers import DefaultRouter

from watchlist_app.api.views import (WatchListAV, WatchDetailAV,
                                     StreamPlatformAV, StreamPlatformDetailAV,StreamPlatformVS,
                                     ReviewAV, ReviewDetailAV, ReviewCreateAV)


router = DefaultRouter()
router.register('platform', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='watch-detail'),
    
    path('',include(router.urls)),
    
    # what inside router doing the same of both these urls
    #  path('platforms/', StreamPlatformAV.as_view(), name='platform-list'),
    # path('platform/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    
    #    path('reviews/', ReviewAV.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetailAV.as_view(), name='review-detail'),
    
    # to get all reviews to specific watch
     path('<int:pk>/reviews', ReviewAV.as_view(), name='review-list'),
     
     # to create a new review for a specific watch
       path('<int:pk>/review-create', ReviewCreateAV.as_view(), name='review-create'),
     
     # to get a specific review
    path('review/<int:pk>/', ReviewDetailAV.as_view(), name='review-detail'),
    
]