from django.conf.urls import url
import views
urlpatterns=[
    url(r"^register/$",views.register),
    url(r"^register_check/$",views.register_check),
    url(r"^register_valid/$",views.register_valid),
    url(r"^login/$",views.login),
    url(r'^login_check2/$',views.login_check2),

    url(r"^login_handle/$",views.login_handle),
    url(r"^user_center_info/$",views.user_center_info),
    url(r"^user_center_site/$",views.user_center_site),
    url(r"^user_center_order/$",views.user_center_order),
    url(r"^logout/$",views.logout)
]