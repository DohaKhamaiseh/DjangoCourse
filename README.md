# DjangoCourse

# Author: Doha Khamaiseh

## WHY?
**This Repository is created for learning purposes. The content is from this course: https://learning.oreilly.com/videos/build-rest-apis/9781801819022/9781801819022-video1_1/**

## WHAT?
**This a IMDB site where the admin user can add streamplatforms and watches and the normal user can add a reviews for that watches**


## How?

1. Account:
    * to register use this link: http://127.0.0.1:8000/accounts/register/
    * to login use this link: http://127.0.0.1:8000/accounts/login/
    * to logout use this link: http://127.0.0.1:8000/accounts/logout/

2. Stream Platforms:
      * to create a streamplatform and get the list of it:  http://127.0.0.1:8000/watch/platforms
      * to get individual streamplatform, update and delete: http://127.0.0.1:8000/watch/platform/streamplatform-id/

3. Watch List:
     * to create a watch and get the list of it:  http://127.0.0.1:8000/watch/list
      * to get individual watch, update and delete: http://127.0.0.1:8000/watch/watch-id/

4. Review:
      * to create a review for a specific watch:  http://127.0.0.1:8000/watch/watch-id/review-create

    * to get all reviews for specific watch: 
    http://127.0.0.1:8000/watch/watch-id/reviews

    * to get individual watch, update and delete: http://127.0.0.1:8000/watch/review/review-id/

## For Learning Purpose:

### Serialization and deserialization process

![Serialization](./public/serilaze.png)
![Serialization](./public/serialize2.png)


### Basic Authentication using Postman:

**After adding the authentication in settings.py and adding a permission for any view we should be a logged in user to get review for example
and to be logged in user using postman is to send user info using Headers bar but the user info should be in base64 encoded format**

Before Encoding:
![Before](./public/auth1.png)

After Encoding:
![After](./public/auth2.png)

### A website to convert to Base64: https://www.base64encode.org/

### Token Authentication using Admin panel: 

![admin](./public/token_auth1.png)

### Token Authentication using Postman: 

#### Copy the token from the Admin panel:

#### Here I send GET request to ReviewDetail View which is using ReviewUserOrReadOnly permission(only the review user can edit) and login with token of Sara user while the review user is doha(its okay because its GET request)

![Sara](./public/GET_Not.png)

###  Here if the request is PUT(the review user(doha) can only edit) and the token is for Sara user

![Sara](./public/PUT_Not.png)

###  Here if the request is PUT(the review user(doha) can only edit) and the token is for doha user

![Doha](./public/PUT.png)


### Create a URL take the username and password and get the token:

![Token](./public/gen_token.png)

### Create a URL to add User

![User](./public/register.png)


### JWT Authentication using Postman: 

### Create a URL take the username and password and get the pair token:

![pair](./public/pair_token.png)

### Before Access Token expired:

![Before](./public/access_before_5m.png)

### After Access Token expired:

![After](./public/access_after_5m.png)


### Create a URL take the Refresh  token to get a new Access token after expired:

![New Access](./public/new_access.png)

### The second request for Reviewlist(not authenticated), the first request already done(we allow for 1 anon request per day)

![Anon_throttling](./public/anon_throttling.png)

### The response after using Pagination

![Page number Pagination](./public/pagination.png)