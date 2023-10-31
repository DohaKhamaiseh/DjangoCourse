# DjangoCourse

## Serialization and deserialization process
![Serialization](./public/serilaze.png)
![Serialization](./public/serialize2.png)


# Basic Authentication using Postman:
**After adding the authentication in settings.py and adding a permission for any view we should be a logged in user to get review for example
and to be logged in user using postman is to send user info using Headers bar but the user info should be in base64 encoded format**

Before Encoding:
![Before](./public/auth1.png)

After Encoding:
![After](./public/auth2.png)

## A website to convert to Base64: https://www.base64encode.org/

# Token Authentication using Admin panel: 

![admin](./public/token_auth1.png)

# Token Authentication using Postman: 
## Copy the token from the Admin panel:
### Here I send GET request to ReviewDetail View which is using ReviewUserOrReadOnly permission(only the review user can edit) and login with token of Sara user while the review user is doha(its okay because its GET request)
![Sara](./public/GET_Not.png)

###  Here if the request is PUT(the review user(doha) can only edit) and the token is for Sara user
![Sara](./public/PUT_Not.png)

###  Here if the request is PUT(the review user(doha) can only edit) and the token is for doha user
![Doha](./public/PUT.png)


## Create a URL take the username and password and get the token:
![Token](./public/gen_token.png)

## Create a URL to add User
![User](./public/register.png)


# JWT Authentication using Postman: 

## Create a URL take the username and password and get the pair token:
![pair](./public/pair_token.png)

### Before Access Token expired:
![Before](./public/access_before_5m.png)

### After Access Token expired:
![After](./public/access_after_5m.png)


## Create a URL take the Refresh  token to get a new Access token after expired:
![New Access](./public/new_access.png)