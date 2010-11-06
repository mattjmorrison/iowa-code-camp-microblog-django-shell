from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    user = models.ForeignKey(User)
    message = models.CharField(max_length=100)
    insert_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.message
