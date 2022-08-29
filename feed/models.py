from django.db import models


# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=140, null=False, blank=True)

    # how to make post title identifiable
    def __str__(self):
        return self.text
