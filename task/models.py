from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # Нужен для админки
        return self.name
