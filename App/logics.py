import requests
from django.core.cache import cache
from Main import config
import random
from common.keys import VCODE_KEY
def rand_code():
    return "".join([str(random.randint(0,9)) for i in range(6)])
def send_vcode(phonenum):
    """发送验证码"""
    #生产验证码
    vcode=rand_code()
    #设置参数
    params=config.YZX_PARAMS.copy()
    params["mobile"]=phonenum
    params["param"]=vcode
    resp=requests.post(config.YZX_API,json=params)
    if resp.status_code==200:
        result=resp.json()
        if result["msg"]=="OK":
            cache.set(VCODE_KEY %phonenum,vcode,timeout=180)   #添加缓存
            return True
    return False
