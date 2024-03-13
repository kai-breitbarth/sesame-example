from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class EmailLoginForm(forms.Form):
    email = forms.EmailField()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("email",)  # Specify only the email field

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields["password1"].required = False
        self.fields["password2"].required = False
        # If one field gets autocompleted but not the other, our 'neither
        # password or both password' validation will be triggered.
        self.fields["password1"].widget.attrs["autocomplete"] = "off"
        self.fields["password2"].widget.attrs["autocomplete"] = "off"

    def clean_password2(self):
        return self.cleaned_data["password1"]
