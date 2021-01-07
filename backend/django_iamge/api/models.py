from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=40)
    image = models.FileField(upload_to='',null=True)


    def __str__(self):
        return self.title




