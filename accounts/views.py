from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages

from django.contrib.auth.models import auth
class LoginView(View):

    def get(self , request , *args , **kwargs):

        return render(request,"registration/login.html")
    
    def post(self , request , *args , **kwargs):
        print("POST REQUEST::::",request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        if(username != '' and password != ''):
            user = auth.authenticate(username=username, password=password)
            if user is not None: 
                if user.active_user:      
                    auth.login(request, user)
                    return redirect("profile")
                messages.error(request,"You cannot login again")
                return redirect("acnt:login")
            else:
                messages.error(request,"Invalid Credentials")
                return redirect("acnt:login")
        else:
            messages.error(request,"Some field is empty")
            return redirect("acnt:login")
    # else:
    #     return redirect("acnt:login")
