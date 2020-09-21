from django.db import models

# Create your models here.


class PostModel(models.Model):
    title = models.CharField(max_length=200)
    blog = models.CharField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


