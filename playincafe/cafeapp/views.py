from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView ,UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import reverse
from .models import System, User, Status
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView



# Create your views here.
class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'cafeapp/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class SystemAddView(CreateView):
    model = System
    fields = "__all__"
    success_url = "system_detail"
    template_name = "cafeapp/add_system.html"


class SystemDetailView(ListView):
    model = System


class SystemDeleteView(DeleteView):
    model = System
    success_url = reverse_lazy('system_detail')

    # template_name = 'system_confirm_delete.html'

    # def post(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     obj.delete()
    #     return HttpResponseRedirect(reverse("system_detail"))


class AddUserView(CreateView):
    model = User
    fields = ['username', 'mobile_number', 'id_proof', 'email']
    success_url = reverse_lazy("userlist")
    template_name = 'cafeapp/add_user.html'


class UserListView(ListView):
    model = User
    template_name = "cafeapp/user_list.html"


class StatusofSysytems(ListView):
    model = Status
    # fields = ["user_system","user"]
    template_name = 'cafeapp/status_list.html'
    # success_url = "home"
    context_object_name = "objects"