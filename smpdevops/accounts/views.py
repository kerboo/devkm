#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from accounts.models import MyGroups,MyUsers
import json



@login_required()
def index(request):
    hpath1 = "系统首页"
    if not request.session.get('user_name'):
        return HttpResponseRedirect('/')        
    return render(request,'accounts/index.html',locals())



@login_required()
def user_list(request):
    hpath1,hpath2 = "用户管理",'用户列表'
    users_obj = MyUsers.objects.all()
    return render(request,'accounts/userlist.html',locals())


@login_required()
def user_add(request):
    pass
    

#send reset password url to user
def SendResetEmail(request):
    pass

def SysrestUserpassword(request):
    pass
              
    