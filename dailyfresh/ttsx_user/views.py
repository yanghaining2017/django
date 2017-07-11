#coding=utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse
from hashlib import sha1
from models import UserInfo
import user_decorators
import datetime
from ttsx_goods.models import GoodsInfo
# Create your views here.
def register(request):
    #继承
    context={'title':'注册','top':'0'}
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
    #重定向到登录页
    return redirect('/user/login/')

def register_valid(request):
    #接收用户名
    uname=request.GET.get('uname')
    #查询当前用户个数
    data=UserInfo.objects.filter(uname=uname).count()
    #返回json{'valid'：1或0}
    context={'valid':data}
    return JsonResponse(context)

def login(request):
    uname=request.COOKIES.get('uname','')
    context={'title':'登录','uname':uname,'top':'0'}
    return render(request,'user/login.html',context)
#登录判断
def login_check2(request):
    uname=request.POST.get('uname')
    upwd=request.POST.get('upwd')



    ulist=UserInfo.objects.filter(uname=uname)
    if ulist:
        s1 = sha1()
        s1.update(upwd)
        upwd_sha1 = s1.hexdigest()
        if upwd_sha1==ulist[0].upwd:
            return JsonResponse({'check':'2'})

        else:
            return JsonResponse({'check':'1'})
    else:
        return JsonResponse({'check':'0'})

def login_handle(request):
    post=request.POST
    uname=post.get('uname')
    upwd=post.get('upwd')
    ujz = post.get('ujz', 0)
    s1=sha1()
    s1.update(upwd)
    upwd_sha1=s1.hexdigest()

    context={'title':'登录','uname':uname,'upwd':upwd,'top':'0'}
    #如果没有查询到数据则返回[],如果查到数据则返回[UserInfo]
    result=UserInfo.objects.filter(uname=uname)
    if len(result)==0:
        #用户名不存在
        context['error_name']='用户名错误'
        return render(request,'user/login.html',context)
    else:
        if result[0].upwd==upwd_sha1:
            #登录成功
            response=redirect(request.session.get('url_path','/'))
            request.session['uid']=result[0].id
            request.session['uname']=result[0].uname

            #记住用户名
            if ujz=='1':
                response.set_cookie('uname',uname,expires=datetime.datetime.now() + datetime.timedelta(days=14))
            else:
                response.set_cookie('uname','',max_age=-1)
            return response
        else:
            #密码错误
            context['error_pwd']='密码错误'
            return render(request,'user/login.html',context)

def logout(request):
    url=request.session.get('url_path')
    request.session.flush()
    request.session['url_path']=url
    return redirect('/user/login/')

@user_decorators.user_islogin
def user_center_info(request):
    user=UserInfo.objects.get(pk=request.session['uid'])
    gstr=request.COOKIES.get('glance')
    glist=gstr.split(',')[1:]
    goods_list=[]
    for i in glist:
        goods_list.append(GoodsInfo.objects.get(pk=int(i)))
    context={'user':user,'goods':goods_list}
    return render(request,'user/user_center_info.html',context)




@user_decorators.user_islogin
def user_center_site(request):
    user = UserInfo.objects.get(pk=request.session['uid'])
    if request.method=='POST':#post请求,修改当前的用户对像的收货信息
        post=request.POST
        ushou=post.get('ushou')
        uaddress=post.get('uaddress')
        ucode=post.get('ucode')
        uphone=post.get('uphone')

        user.ushou=ushou
        user.uaddress=uaddress
        user.ucode=ucode
        user.uphone=uphone
        user.save()

    context={'user':user}
    return  render(request,'user/user_center_site.html',context)
@user_decorators.user_islogin
def user_center_order(request):
    context={}
    return render(request,'user/user_center_order.html',context)



