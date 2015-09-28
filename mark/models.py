from django.db import models


class Foo(models.Model):
    num = models.IntegerField()
    txt = models.TextField()
