from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class post(models.Model):
    title=models.CharField(max_length=150)
    content=models.TextField()
    timestamp=models.DateTimeField(default=timezone.now())         #post date
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title +' by '+str(self.posted_by)

class contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField()
    message=models.TextField()
    timestamp=models.DateTimeField(default=timezone.now())         #post date
    def __str__(self):
        return self.name