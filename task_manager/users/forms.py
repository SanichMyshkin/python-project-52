from django.contrib.auth.forms import UserCreationForm
from .models import User

from django.core.exceptions import ValidationError


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get("username")
        current_user_id = self.instance.id

        if username:
            user_exists = self._meta.model.objects.filter(
                username__iexact=username
            ).exclude(id=current_user_id).exists()

            if user_exists:
                self._update_errors(
                    ValidationError(
                        {
                            "username": self.instance.unique_error_message(
                                self._meta.model, ["username"]
                            )
                        }
                    )
                )
            else:
                return username
