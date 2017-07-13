#coding=utf-8
from django.shortcuts import render
from .models import CartInfo
from django.http import JsonResponse
# Create your views here.
def index(request):
    context={'title':'购物车'}
    return render(request,'cart/cart.html',context)
def add(request):
    try:
        gid=request.GET.get('gid')
        print(gid)
        uid=request.session.get('uid')
        cart=CartInfo.objects.filter(user__id=int(uid),goods=int(gid))
        if cart:
            cart[0].count+=1
            cart[0].save()
        else:
            new_cart=CartInfo()
            new_cart.user_id=int(uid)
            new_cart.goods_id=int(gid)
            print(gid)
            new_cart.count=1
            new_cart.save()

        return JsonResponse({'result':1})
    except Exception as e:
        print(e)
        return JsonResponse({'result': 0})

