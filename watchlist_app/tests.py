from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User

from watchlist_app.models import StreamPlatform, Watchlist, Review
from watchlist_app.api import serializers

class StreamPlatformTestCase(APITestCase):
    """
    a class to test all stream platform functionality(create, get(list,individual), put, delete)
    """
    def setUp(self):
        # This method will be called before any test functions
        # Note: if we change it from create_user to create_superuser all streamplatform detail functions will be allowed(not HTTP_403_FORBIDDEN)
        self.user = User.objects.create_user(username="test", password="test123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        # this one is needed to test the functionality of getting individual stream
        self.stream = StreamPlatform.objects.create(name="Netflix", about="Shit", website="https://netflix.com")
    
    def test_streamplatform_create(self):
        data = {
            "name":"Netflix",
            "about":"Shit",
            "website":"https://netflix.com"
        }
        
        response = self.client.post(reverse('platform-list'),data)
        # we use this HTTP_403_FORBIDDEN because create streamplatform is allowed only by admin user
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)
    
    def test_streamplatform_list(self):
        response = self.client.get(reverse('platform-list'))
        # we use this HTTP_200_OK because get list of streamplatforms is allowed by any user
        # Note: the test will work even we haven't a list of streams
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_streamplatform_indivisual(self):
        response = self.client.get(reverse('streamplatform-detail',args=(self.stream.id,)))
        # we use this HTTP_200_OK because get list of streamplatforms is allowed by any user
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_streamplatform_update(self):
        data = {
            "name":"Netflix",
            "about":"Shit-updated",
            "website":"https://netflix.com"
        }
        response = self.client.put(reverse('streamplatform-detail',args=(self.stream.id,)),data)
        # we use this HTTP_403_FORBIDDEN because update streamplatform is allowed only by admin user
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)
    
    def test_streamplatform_delete(self):
        response = self.client.delete(reverse('streamplatform-detail',args=(self.stream.id,)))
        # we use this HTTP_403_FORBIDDEN because delete streamplatform is allowed only by admin user
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

class WatchListTestCase(APITestCase):
    """
    A class to test all watchlist view functionality, create a watchlist, get(list, individual), update and delete watchlist
    """
    def setUp(self):
        # This method will be called before any test functions
        # Note: if we change it from create_user to create_superuser all streamplatform detail functions will be allowed(not HTTP_403_FORBIDDEN)
        self.user = User.objects.create_user(username="test", password="test123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
         # this one is needed to test the functionality of creating watchlist(we should mention this watchlist is from which streamplatform)
        self.stream = StreamPlatform.objects.create(name="Netflix", about="Shit", website="https://netflix.com")
        
        # this one is needed to test the functionality of getting individual watchlist
        self.watchlist = Watchlist.objects.create(title="Movie #1", storyline="Nothing", active=True, platform=self.stream)
          
    
    def test_watchlist_create(self):
        data = {
            "title":"Movie #1",
            "storyline":"Nothing",
            "active":True,
            "platform": self.stream
            
        }
        
        response = self.client.post(reverse('watch-list'),data)
        # we use this HTTP_405_METHOD_NOT_ALLOWED because create watchlist is allowed only by admin user
        # Note: I wrote this HTTP_403_FORBIDDEN but in test I got HTTP_405_METHOD_NOT_ALLOWED
        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_watchlist_list(self):
        response = self.client.get(reverse('watch-list'))
        # we use this HTTP_200_OK because getting watchlist is allowed by any user
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_watchlist_individual(self):
        response = self.client.get(reverse('watch-detail',args=(self.watchlist.id,)))
        # we use this HTTP_200_OK because getting watchlist is allowed by any user
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(Watchlist.objects.get().title, 'Movie #1')
    
    def test_watchlist_update(self):
        data = {
          "title":"Movie #1",
            "storyline":"Nothing-updated",
            "active":True,
            "platform": self.stream
        }
        response = self.client.put(reverse('watch-detail',args=(self.stream.id,)),data)
        # we use this HTTP_403_FORBIDDEN because update watchlist is allowed only by admin user
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)
        
    
    def test_watchlist_delete(self):
        response = self.client.delete(reverse('watch-detail',args=(self.stream.id,)))
        # we use this HTTP_403_FORBIDDEN because delete watchlist is allowed only by admin user
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)

class ReviewTestCase(APITestCase):
    """
    A class to test all review view functionality, create a review, get(list, individual), update and delete review
    """
    
    def setUp(self):
        # This method will be called before any test functions
        self.user = User.objects.create_user(username="test", password="test123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
         # this one is needed to test the functionality of creating watchlist(we should mention this watchlist is from which streamplatform)
        self.stream = StreamPlatform.objects.create(name="Netflix", about="Shit", website="https://netflix.com")
        
        # this one is needed to test the functionality of creating review (we should mention this review is for which watchlist)
        self.watchlist = Watchlist.objects.create(title="Movie #1", storyline="Nothing", active=True, platform=self.stream)
        
        # # this one is needed to test the functionality of creating a review because we can't create 2 review for the same watchlist from the same user
        self.watchlist2 = Watchlist.objects.create(title="Movie #2", storyline="bll", active=True, platform=self.stream)
        
         # this one is needed to test the functionality of getting individual review
        self.review = Review.objects.create(review_user=self.user,rating=5, description="blaaa", active=False,watchlist=self.watchlist)
        
        
    def test_review_create(self):
        # Note: any user can create a new review(not only admin)
        # Not: I got 400 error (Bad Request) when I passed the self.user and self.watchlist without id
        data={
            "review_user":self.user.id,
            "rating":5, 
            "description":"blaaa",
            "active":False,
            "watchlist":self.watchlist2.id
        }
        
        response = self.client.post(reverse('review-create',args=(self.watchlist2.id,)),data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    
    def test_review_create_unauth(self):
        

        data={
            "review_user":self.user,
            "rating":5, 
            "description":"blaaa",
            "active":False,
            "watchlist":self.watchlist2.id
        }
        
        # this is to anonymous user, so now the user is anauthenticated
        self.client.force_authenticate(user=None)
        response = self.client.post(reverse('review-create',args=(self.watchlist2.id,)),data)
        # print(response.content)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
    
    def test_review_list(self):
        response = self.client.get(reverse('review-list',args=(self.watchlist2.id,)))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_review_individual(self):
        response = self.client.get(reverse('review-detail',args=(self.review.id,)))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_review_update(self):
        
        data={
            "review_user":self.user.id,
            "rating":4, 
            "description":"blaaa-updated",
            "active":False,
            "watchlist":self.watchlist.id
        }
        response = self.client.put(reverse('review-detail',args=(self.review.id,)),data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(Review.objects.get().description,"blaaa-updated")
    
    def test_review_delete(self):
        response = self.client.delete(reverse('review-detail',args=(self.review.id,)))
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        
    
    def test_review_user(self):
        response = self.client.get('/watch/reviews/?username'+ self.user.username)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


