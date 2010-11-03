from django.db import models

class Microblog(models.Model):
    message = models.CharField(max_length=160)
    post_time = models.DateTimeField(auto_now=True)

    @staticmethod
    def add_message(message):
        if len(message) > 160:
            raise ValueError("message length is too long")
        Microblog.objects.create(message=message)

    @staticmethod
    def timeline():
        return Microblog.objects.all().order_by('-post_time')