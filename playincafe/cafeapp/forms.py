from django import forms
from .models import User, System, History
from django.contrib.messages.views import SuccessMessageMixin
from .choices import STATUS, OCCUPIED


class StatusForm(forms.ModelForm):
    # status = forms.ChoiceField(choices=STATUS)

    class Meta:
        model = History
        fields = ["user_history", "system_name"]

    def __init__(self, *args, **kwargs):
        super(StatusForm, self).__init__(*args, **kwargs)
        self.fields['system_name'].queryset = System.objects.filter(status="Available")


""" Allot system form """
# class StatusListofSysytemsForm(forms.ModelForm):
#     class Meta:
#         model = System
#         fields ="__all__"



class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'mobile_number', 'id_proof', 'email']
