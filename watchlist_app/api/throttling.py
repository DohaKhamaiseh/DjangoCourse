from rest_framework.throttling import UserRateThrottle

# This is for custom throttling

class ReviewAVThrottle(UserRateThrottle):
    scope = 'review-list'
    

class ReviewCreateAVhrottle(UserRateThrottle):
        scope = 'review-create'