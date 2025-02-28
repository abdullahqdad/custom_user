from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class ChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']