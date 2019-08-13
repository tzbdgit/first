from django.conf.urls import url

from check import views

urlpatterns=[
    url(r"index/",views.index),
    url(r"^smsg/",views.send_sms),
    url(r'^send_message$', views.send_message, name='send_message'),
]