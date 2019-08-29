from django.conf.urls import url

from App import views

urlpatterns=[
    url(r"^send_msg/",views.send_msg),
    url(r"^check_vcode/",views.check_vcode),
    url(r"get_profile/",views.get_profile)
]