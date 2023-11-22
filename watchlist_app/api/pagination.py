from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class WatchListPagination(PageNumberPagination):
    """
       This is a custom Page Number pagination for WatchList
    """
    # the link will be like this: http://127.0.0.1:8000/watch/list/?page=2
    page_size = 5
    
    # this is to override the page number name, the link will be like this: http://127.0.0.1:8000/watch/list/?p=2
    # if the page is the first one the link will be like this: http://127.0.0.1:8000/watch/list/
    page_query_param = 'p'
    
    # this is to override the page size, the link will be like this: http://127.0.0.1:8000/watch/list/?p=2&size=10
    # if the page is the first one the link will be like this: http://127.0.0.1:8000/watch/list/?size=10
    page_size_query_param = 'size'
    
    # this is to restrict the maximum number of elements per page
    # so if the user didn't pass the size parameter the size will be 5 and if he wanna to pass it the maximum value can be 10
    # Note: If he passed more than 10 will not give him error but will only load 10 elements per page 
    max_page_size = 10
    
    # this is to access directly the last page, but by default we can access it like this:  http://127.0.0.1:8000/watch/list/?p=last
    last_page_strings = 'end'
    # now the link to access the last page directly will be like this: http://127.0.0.1:8000/watch/list/?p=end  , and if we pass last will get:
    #  'invalid page'
    
    
class WatchListLOPagintaion(LimitOffsetPagination):
    """
    this is the custom Limit Offset Pagination for watch list
    """
    
    # limit : is the page size , offset: the number of records you wish to skip before selecting records
    
    # this is refer to the number of elements per page, the link will be like this: http://127.0.0.1:8000/watch/list/?limit=5&offset=5
    # the link before is for page #2 so the page will have 5 elements and we should skip 5 elements to reach page #2
    # the link for the first page will be like this: http://127.0.0.1:8000/watch/list/?limit=5 , no elements to skip(no offset)
    # Note: we can change the value of limit and offset from the link itself(on Postman)
    default_limit = 5
    
    # this is to restrict the maximum number of elements per page
    # so if the user didn't pass the size parameter the size will be 5 and if he wanna to pass it the maximum value can be 10
    # Note: If he passed more than 10 will not give him error but will only load 10 elements per page 
    max_limit = 10
    
    # this is to override the limit(page number)name from 'limit to 'lmt',the link will be like this: http://127.0.0.1:8000/watch/list/?lmt=5&start=5
    # the standard leave it as 'limit'
    limit_query_param = 'lmt'
    
    # this is to override the  offset(number of elements to skip) name from 'offset' to 'start'
    offset_query_param  = 'start'
    
class WatchListCPagination(CursorPagination):
    # on Postman  the link will be like this: http://127.0.0.1:8000/watch/list/?cursor=cD0yMDIzLTExLTA0KzEyJTNBMjUlM0EzMi41MzM2NjclMkIwMCUzQTAw
    # after cursor params is generated randomly
    # on the browser its looks like this: <<Previous  Next>>  to click on  
    page_size  = 5
    
    # the value of this is by default descending created(is a attribute from watchlist model) : ordering= -created(new to old)
    # Now its acending order according to created attribute(its the standard attribute to use), we can use any attribute
    ordering = 'created'
    
    # this to override the cursor params from 'cursor' to 'record'
    # on Postman  the link will be like this: http://127.0.0.1:8000/watch/list/?record=cD0yMDIzLTExLTA0KzEyJTNBMjUlM0EzMi41MzM2NjclMkIwMCUzQTAw
    cursor_query_param  = 'record'
    