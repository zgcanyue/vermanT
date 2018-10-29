from django.http import HttpResponseRedirect
from django.contrib.auth import SESSION_KEY
from urllib.request import quote
import sys
from  django.conf import settings
from django.views.debug import technical_500_response
# class LoginAuthenticationMiddleware(object):
#     def process_request(self,request):
#         if not request.user.is_authenticated:
#             return HttpResponseRedirect('/verman/login/')
from django.shortcuts import redirect


# class LoginAuthenticationMiddleware(object):
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         if request.path.startswith('/verman'):
#             return None
#         if request.path.startswith('/verman'):
#             return redirect('/verman/login/')

class UserBasedExceptionMiddleware(object):
    def process_exception(self,request,exception):
        if request.user.is_superuser or request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS:
            return technical_500_response(request,*sys.exc_info())
        return exception