from django.db import models


class Blog(models.Model):
    key = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=240)
