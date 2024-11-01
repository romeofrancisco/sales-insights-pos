from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email','username','role']

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email','username','role']