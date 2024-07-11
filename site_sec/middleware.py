from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse

class CsrfExemptAdminMiddleware(MiddlewareMixin):
    def process_view(self, request, callback, callback_args, callback_kwargs):
        if request.path.startswith(reverse('admin:index')):
            setattr(request, '_dont_enforce_csrf_checks', True)
        return None