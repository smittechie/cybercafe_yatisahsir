from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import reverse
from .models import System, User, Status
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView, View
from .forms import StatusForm, AddUserForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'cafeapp/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class SystemAddView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = System
    fields = "__all__"
    success_url = "system_detail"
    template_name = "cafeapp/add_system.html"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        messages.success(self.request, "System added sucess fully ")
        return super().form_valid(form)


class SystemDetailView(LoginRequiredMixin, ListView):
    model = System
    login_url = 'login'


class SystemDeleteView(LoginRequiredMixin, DeleteView):
    model = System
    success_url = reverse_lazy('system_detail')
    login_url = 'login'

    # template_name = 'system_confirm_delete.html'
    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.delete()
        messages.warning(self.request, "User deleted")
        return HttpResponseRedirect(success_url)



class AddUserView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = User
    # fields = ['username', 'mobile_number', 'id_proof', 'email']
    success_url = reverse_lazy("userlist")
    template_name = 'cafeapp/add_user.html'
    form_class = AddUserForm

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        messages.success(self.request, "User added")
        return super().form_valid(form)


class UserListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = User
    template_name = "cafeapp/user_list.html"

class UpdateUserview(UpdateView):
    model = User
    fields = ['username', 'mobile_number', 'id_proof', 'email']
    template_name = 'cafeapp/user_update.html'
    success_url = reverse_lazy("userlist")


class StatusofSysytems(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Status
    fields = "__all__"
    template_name = 'cafeapp/status_allot.html'
    success_url = "/alloted_system_list/"

    # context_object_name = "objects"

    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = StatusForm()
        return context


class StatusListofSysytems(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Status
    template_name = 'status_list.html'
