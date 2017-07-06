from django.conf.urls import url
import views
urlpatterns=[
    url(r"^register/$",views.register),
    url(r"^register_check/$",views.register_check),
    url(r"^register_valid/$",views.register_valid),
    url(r"^login/$",views.login),
    url(r"^login_handle/$",views.login_handle),
    url(r"^user_center_info/$",views.user_center_info),
]