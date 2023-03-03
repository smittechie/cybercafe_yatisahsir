from datetime import datetime
from time import timezone
import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import reverse
from .models import System, User, History
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView, View
from .forms import AddUserForm, StatusForm, ReleaseViewForm  # , StatusListofSysytemsForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .choices import STATUS


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
    fields = ['name', 'graphic_card', 'processor', 'ram', 'ram_unit']
    success_url = "system_detail"
    template_name = "cafeapp/add_system.html"

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        # profile = form.save(commit=False)
        # self.object = self.name
        # self.object.save()
        messages.success(self.request, "System added successfully ")
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


class AllotmentofSystemsView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = History
    fields = '__all__'
    template_name = 'cafeapp/status_allot.html'

    # context_object_name = "objects"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = StatusForm()
        return context

    def post(self, request, *args, **kwargs):
        print("post method calling.......")
        print(request.POST)
        used_system_id = (request.POST.get('system_name'))  ### system(computer) used  in History model

        user_id = (request.POST.get('user_history'))  ### useer used in History model

        object_of_status = System.objects.get(id=used_system_id)
        object_of_status.status = "Occupied"
        object_of_status.save()

        username_history = User.objects.get(id=user_id)
        print(username_history)
        # usernameinhistory = History.objects.all().filter(user_history =username_history )
        # print(usernameinhistory)
        logtime = datetime.datetime.now()
        print(logtime)
        History.objects.create(user_history=username_history, system_name=object_of_status)
        return redirect(reverse('sysytemstatuslist'))


class StatusListofSysytems(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = History
    template_name = 'cafeapp/status_list.html'

    def get_queryset(self):
        # queryset = History.objects.filter(is_deleted=False)

        queryset = History.objects.all().exclude(user_history=None)
        return queryset


class ReleaseView(UpdateView):
    model = History
    # fields = ['user_history','system_name']
    template_name = 'cafeapp/release.html'
    success_url = reverse_lazy("sysytemstatuslist")
    form_class = ReleaseViewForm

    def post(self, request, *args, **kwargs):
        systemid= request.POST.get("system_name")
        sysobj = System.objects.get(id = systemid)
        sysobj.status = 'Available'
        sysobj.save()
        self.object = self.get_object()
        self.object.is_deleted = True
        logouttime = datetime.datetime.now()
        self.object.logout_time = logouttime
        self.object.save()

        return super().post(request, *args, **kwargs)


class HistoryListView(ListView):
    model = History
