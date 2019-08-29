from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render
from App import logics
# Create your views here.
from App.models import Person
from common import keys
from common import stat
from libs.http import render_json


def send_msg(request):
    phonenum=request.GET.get("phonenum")
    if cache.get(keys.VCODE_KEY%phonenum):
        return render_json(code=stat.OPT_REPEAT,data="请不要重复操作")
    if logics.send_vcode(phonenum):
        return render_json(code=stat.OK,data=None)
    else:
        return render_json(code=stat.SMS_ERR,data="短信发送失败")


def check_vcode(request):
    """检查验证码，兵登陆或注册"""
    phonenum=request.POST.get("phonenum")
    vcode=request.POST.get("vcode")
    cache_vcode=cache.get(keys.VCODE_KEY %phonenum)
    if not cache_vcode:
        return render_json(code=stat.VCODE_EXPIRE,data="验证码已过期")
    if cache_vcode==vcode:
        """从数据库获得或创建用户"""
        try:
            user=Person.objects.get(phonenum=phonenum)
        except Person.DoesNotExist:
            user=Person()
            user.phonenum=phonenum
            user.nickname="adc"
            user.save()
         #"执行登陆"
        request.session["uid"]=user.id
        return render_json(code=stat.OK,data=user.to_dict())
    else:
        return render_json(code=stat.VCODE_ERR,data="验证码错误")


def get_profile(request):
    user=request.user
    print(type(user))#<class 'App.models.Person'>
    return render_json(data=user.to_dict())#由于忘记写（）,导致这个方法没有被调用,报错Object of type 'method' is not JSON serializable



