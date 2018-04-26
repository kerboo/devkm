#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from accounts import forms
from accounts.models import History_Login
import json




#login in
def Login(request):
    restdata = {'data':'','errors':''}
    loginform = forms.SimpleLogin()
    restdata['data'] = loginform
    if request.method == 'POST':
        checkform = forms.SimpleLogin(request.POST)        
        if checkform.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            print username,password
            user = authenticate(username=username,password=password)
            if not request.POST.get('remember_me',None):
                request.session.set_expiry(0)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    request.session['user_name'] = user.username
                    request.session['user_id'] = user.id
                    history_login = History_Login(
                        user=user,
                        user_ip = request.META['REMOTE_ADDR'],
                        request_method=request.META['REQUEST_METHOD'],
                        request_url=request.META['HTTP_REFERER'],
                    )
                    history_login.save()
                    msg={'msginfo':'login is ok'}
                    return HttpResponse(json.dumps(msg))
                else:
                    msg = {'msgerror':u"登录失败"}
                    return HttpResponse(json.dumps(msg))
            else:
                msg = {'msgerror':u"登录失败"}
                return HttpResponse(json.dumps(msg))
        else:
            restdata['data'] = checkform
            restdata['error'] = checkform.errors.as_data().values()[0][0].messages[0]
    return render(request,'login.html',restdata) 


#logout
def Logout(request):
    logout(request)
    if request.session.get('user_name'):
        del request.session['user_name']
    return HttpResponseRedirect('/',)
