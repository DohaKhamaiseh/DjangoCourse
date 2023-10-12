from django.urls import path, include
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='watch-detail'),
     path('platforms/', StreamPlatformAV.as_view(), name='platform-list'),
    path('platform/<int:pk>/', StreamPlatformDetailAV.as_view(), name='platform-detail'),
]