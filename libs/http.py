from django.conf import settings
from django.http import HttpResponse
import json

def render_json(data,code=0):
    result={
        "data":data,
        "code":code,
    }
    if settings.DEBUG:
        json_str=json.dumps(result,indent=4,
                            sort_keys=True,
                            ensure_ascii=False,
                            )
    else:
        json_str = json.dumps(result,
                              separators=[",",":"],
                              ensure_ascii=False,
                              )

    return HttpResponse(json_str)