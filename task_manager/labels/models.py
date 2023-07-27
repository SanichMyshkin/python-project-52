from django.db import models
from task_manager.translations.trans import NameForField

names = NameForField()


class Label(models.Model):
    time_create = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255,
                            verbose_name=names.name)

    class Meta:
        verbose_name = names.label
        verbose_name_plural = names.labels

    def __str__(self):
        return self.name
