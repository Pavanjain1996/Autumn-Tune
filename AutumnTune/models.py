from django.db import models

class File(models.Model):
    name = models.CharField(max_length=100)
    singer = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    actress = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    date = models.DateTimeField()
    language = models.CharField(max_length=100,default='Hindi')
    category = models.CharField(max_length=100,default='Party')
    typeof = models.CharField(max_length=100,default='Singing')

    def __str__(self):
        return self.name

class UserData(models.Model):
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100,default='')
    lname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.fname+' '+self.mname+' '+self.lname
