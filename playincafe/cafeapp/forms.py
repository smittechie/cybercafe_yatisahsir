from django import forms
from .models import Status, User, System
from django.contrib.messages.views import SuccessMessageMixin
from .choices import STATUS, OCCUPIED


class StatusForm(forms.ModelForm):
    status = forms.ChoiceField(choices=STATUS)

    class Meta:
        model = Status
        fields = ['user_system', "user", "status"]

    def __init__(self, *args, **kwargs):
        super(StatusForm, self).__init__(*args, **kwargs)
        self.fields['user_system'].queryset = System.objects.filter(status="Available")


class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'mobile_number', 'id_proof', 'email']
