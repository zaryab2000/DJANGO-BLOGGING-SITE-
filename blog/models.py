from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    article = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    image = models.FileField(upload_to='blog_pics')
    public = models.BooleanField(default=False,blank=False)
    person = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
