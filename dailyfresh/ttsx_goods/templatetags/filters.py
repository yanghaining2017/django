#coding=utf-8
#引入注册对象
from django.template import Library
register=Library()

#使用装饰器进行注册
@register.filter
def num1(value):
    if value != -1 and value != 1:
        return 1
    else:
        return value