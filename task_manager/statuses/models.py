from django.db import models
from task_manager.translations.trans import NameForField

names = NameForField()


class Status(models.Model):
    time_create = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, unique=True,
                            verbose_name=names.name)

    def __str__(self):
        return self.name
