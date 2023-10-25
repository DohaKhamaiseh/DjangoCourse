from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    
    # the difference between has_permission and has_object_permission is that the second one specifies for certain object from that model(need id)
    
    def has_permission(self, request, view):
        # this line wil return True if the user is Admin(by check request.user and request.is_staff).
        # return super().has_permission(request, view)
        
        admin_permission = bool(request.user and request.user.is_staff)
        
        # this line will return True if the user is Admin or the method is get(no edit)
        return admin_permission or request.method =="GET" 
    
class ReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
           # Check permissions for read-only request
           return True
        else:
            # Check permissions for write request
            # this line will check that user who want ot edit is the same user who has the review?
            return request.user == obj.review_user