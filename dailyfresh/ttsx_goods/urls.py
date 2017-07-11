from django.conf.urls import url
import views
urlpatterns=[

    url(r'^index/$',views.index),
    url(r'^list(\d?)(\d*)',views.goods_list),
    url(r'^detail(\d+)/$',views.detail),

]