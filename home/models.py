from django.db import models
from django.utils import timezone

class Test(models.Model):
    inFile = models.FileField()
    outFile = models.FileField()
    score = models.IntegerField()


class Problem(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, primary_key=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
