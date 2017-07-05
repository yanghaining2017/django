#coding=utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse
from hashlib import sha1
from models import UserInfo
# Create your views here.
def register(request):
    #继承
    context={'title':'注册'}
    return render(request,'user/register.html',context)

def register_check(request):
    #接受用户请求
    post=request.POST
    uname=post.get('uname')
    upwd=post.get('upwd')
    ucpwd=post.get('ucpwd')
    uemail=post.get('uemail')
    #密码加密
    s1=sha1()
    s1.update(upwd)
    upwd_sha1=s1.hexdigest()
    #向数据库保存数据
    user=UserInfo()
    user.uname=uname
    user.upwd=upwd_sha1
    user.umail=uemail
    user.save()
    return redirect('/user/login/')

def register_valid(request):
    uname=request.GET.get('uname')
    data=UserInfo.objects.filter(uname=uname).count()
    context={'valid':data}
    return JsonResponse(context)





