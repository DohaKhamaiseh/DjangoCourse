from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class StreamPlatform(models.Model):
    """
    this is the platform that streams the watchlist
    """
    name = models.CharField(max_length=50)
    about = models.TextField(max_length=50)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Watchlist(models.Model):
    """
    its can be movie on cinema, podcast show, movie on TV or others.
    """
    title = models.CharField(max_length=50)
    # storyline its like description
    storyline = models.CharField(max_length=200)
    # its refer if the watch is realised or not
    
    # each watch hosted by one platform
    # related_name mean : 
    # Without a related_name, if you wanted to access all the instances of Watchlist related to a particular StreamPlatform instance, you would use the default reverse relation name  which is lowercase model name followed by "_set". For instance: stream_platform_instance.mymodel_set.all()
    # but with related_name it will be like this: stream_platform_instance.watchlist.all()
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    """
    each watch has one or more reviews, but each review is for a specific watch
    """
    
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE, related_name="reviews")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.rating) + " -" + self.watchlist.title
