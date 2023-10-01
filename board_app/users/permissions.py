from rest_framework import permissions

class CustomReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # permissions.SAFE_METHODS : 데이터에 영향을 미치지 않는 메소드
            return True
        # PUT/PATCH
        return obj.user == request.user