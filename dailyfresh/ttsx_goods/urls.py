from django.conf.urls import url
import views
urlpatterns=[

    url(r'^index/$',views.index),
    url(r'^list(\d+)/$',views.goods_list),

]