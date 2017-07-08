#coding=utf-8
from django.shortcuts import render
from models import *
# Create your views here.

def index(request):
    type_list=TypeInfo.objects.all()
    list1=[]
    for type1 in type_list:
        new_list=type1.goodsinfo_set.order_by('-id')[0:4]
        click_list=type1.goodsinfo_set.order_by('-gclick')[0:4]
        list1.append({'new_list':new_list,'click_list':click_list,'t1':type1})
    context={'list1':list1,'title':'首页'}
    return render(request,'ttsx_goods/index.html',context)

def goods_list(request):
    t1=TypeInfo.objects.get(pk=int(tid))
    new_list=t1.goodsinfo_set.order_by('-id')[0:2]
    glist=t1.goodsinfo_set.order_by('-id')
    context={'cart_show':1}
    return render(request,'ttsx_goods/list.html',context)









