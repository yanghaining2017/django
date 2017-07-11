#coding=utf-8
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import GoodsInfo,TypeInfo
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

def goods_list(request,tid,pindex):
    if not pindex:
        pindex=1
    pindex=int(pindex)
    if not tid:
        tid=1

    desc=request.GET.get('desc','0')
    desc=int(desc)*-1


    if desc == -1:
        cla = {'gprice': 'active'}
        str='gprice'
    elif desc == 1:
        cla = {'gprice': 'active'}
        str = '-gprice'
    elif desc == 0:
        cla = {'default': 'active'}
        str = '-id'
    else:
        cla = {'gclick': 'active'}
        str = '-gclick'
        print(str)
    t1=TypeInfo.objects.get(pk=int(tid))
    new_list=t1.goodsinfo_set.order_by(str)[0:2]
    glist=t1.goodsinfo_set.order_by(str)

    paginator = Paginator(glist, 5)
    page = paginator.page(pindex)
    num=page.paginator.num_pages
    # left=pindex//5*5+1
    # right=(pindex//5+1)*5+1
    # if pindex % 5 == 0:
    #     left -= 5
    #     right -= 5
    left=pindex-2
    right=pindex+3
    if left<1:
        left=1
    if num < right:
        right = num+1


    alist=range(left,right)

    context = {'cart_show': '1', 'title': '商品列表', 't1': t1,
               'new_list': new_list, 'page': page,'alist':alist,
               'num':desc,'cla':cla}
    return render(request, 'ttsx_goods/list.html', context)



def detail(request,id):
    # try:
    goods=GoodsInfo.objects.get(pk=int(id))
    print(goods)
    goods.gclick+=1
    goods.save()

    new_list=goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context={'cart_show':'1','title':'商品详细信息','new_list':new_list,'goods':goods}
    gstr = request.COOKIES.get('glance','')
    gstr+= ",%s"%goods.id




    response= render(request,'ttsx_goods/detail.html',context)
    response.set_cookie('glance',gstr)
    return response
    # except:
    #     return render(request,'404.html')









