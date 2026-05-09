from django.core.exceptions import PermissionDenied

def employer_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.role != 'employer':
            raise PermissionDenied("You are not an employer")
        return view_func(request, *args, **kwargs)
    return wrapper