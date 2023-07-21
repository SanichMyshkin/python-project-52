from django.contrib.auth.forms import UserCreationForm
from .models import TaskUser


class UserForm(UserCreationForm):
    class Meta:
        model = TaskUser
        fields = ('username', 'first_name', 'last_name',
                  'password1', 'password2')
