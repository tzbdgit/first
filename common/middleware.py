from django.utils.deprecation import MiddlewareMixin

from App.models import Person
from common import stat
from libs.http import render_json


class AuthMiddleware(MiddlewareMixin):
    API_WHITE_LIST=[
        "/App/send_msg/",
        "/App/check_vcode/",
    ]
    def process_request(self,request):
        print(request.path)
        if request.path in self.API_WHITE_LIST:
            return
        uid=request.session.get("uid")
        if not uid:
            return render_json(code=stat.LOGIN_REQUIRED,data="需要登陆")
        else:
            request.user=Person.objects.get(id=uid)