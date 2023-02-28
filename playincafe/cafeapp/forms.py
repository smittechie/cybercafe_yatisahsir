from django import forms
from .models import Status, User
from django.contrib.messages.views import SuccessMessageMixin
from .choices import STATUS, OCCUPIED


class StatusForm(forms.ModelForm):
    status = forms.ChoiceField(choices=STATUS)

    class Meta:
        model = Status
        fields = ['user_system', "user", "status"]

    def save(self, commit=True):
        inst = super().save(commit)
        inst.status = OCCUPIED
        inst.save()
        return inst




class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'mobile_number', 'id_proof', 'email']
