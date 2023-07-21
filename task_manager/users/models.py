# from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class TaskUser(User):

    def __str__(self):
        return " ".join((str(self.first_name), str(self.last_name)))

