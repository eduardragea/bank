from django.conf import settings
from django.shortcuts import redirect

def login_prohibited(view_function):
    def modified_view_function(request):
        if request.user.is_authenticated:
            redirect_url = 'dashboard'
            return redirect(redirect_url)
        else:
            return view_function(request)
    return modified_view_function
