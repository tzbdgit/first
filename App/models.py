import datetime

from django.db import models

# Create your models here.
class Person(models.Model):
    SEX=(
        ("male","男"),
        ("female","女"),
    )
    LOCATION=(
        ("北京","北京"),
        ("上海","上海"),
        ("合肥","合肥")
    )
    phonenum=models.CharField(max_length=16,unique=True,db_index=True)
    nickname=models.CharField(max_length=32)
    sex=models.CharField(max_length=8,choices=SEX)
    birthday=models.DateField(default=datetime.date(1990,1,1))
    avatar=models.CharField(max_length=256)
    location=models.CharField(max_length=16,choices=LOCATION)
    def to_dict(self):
        return {"phonenum":self.phonenum,
                "nickname":self.nickname,
                "sex":self.sex,
                "birthday":str(self.birthday),
                "avatar":self.avatar,
                "location":self.location}

