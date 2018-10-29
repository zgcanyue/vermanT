import json
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#可以放弃
# class User(models.Model):
#     username = models.CharField(max_length=20,default='test')
#     password = models.CharField(max_length=20)
#
#     def __unicode__(self):
#         return self.username
#     def __str__(self):
#         return self.username

class AppDate(models.Model):
    app_name = models.CharField(max_length=50)
    adnroid =models.CharField(max_length=50)
    ios = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    test_account = models.CharField(max_length=50)

    def __str__(self):
        return json.dumps({"id":self.id,"app_name":self.app_name,"adnroid":self.adnroid,
                           "ios":self.ios,"address":self.address,"test_account":self.test_account })

class User1(User):

    def __str__(self):
        return json.dumps({'id':self.id,'username':self.username,'email':self.email})
