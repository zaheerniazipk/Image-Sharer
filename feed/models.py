from django.db import models
from sorl.thumbnail import ImageField


# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=140, null=False, blank=True)
    image = models.ImageField()

    # how to make post title identifiable
    def __str__(self):
        return self.text
