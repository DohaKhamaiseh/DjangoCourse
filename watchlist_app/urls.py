from django.urls import path, include
from watchlist_app.views import WatchListView, WatchDetailView

urlpatterns = [
    path('list/', WatchListView, name='movie-list'),
    path('<int:pk>/', WatchDetailView, name='movie-detail'),
]