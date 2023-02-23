from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import reverse
from .models import System
from django.http import HttpResponseRedirect

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


class SystemDetailView(ListView):
    model = System


class SystemDeleteView(DeleteView):
    model = System
    sucess_url = 'system_detail'

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return HttpResponseRedirect(reverse("system_detail"))
    # template_name = 'geeksmodel_confirm_delete.html"'

    # def get(self, request, *args, **kwargs):
    #     some_var = request.POST
    #     print(request.POST)
    #     self.object = self.get_object()
    #     context = self.get_context_data(object=self.object)
    #     return self.render_to_response(context)

# from django.http import HttpResponseRedirect
# from django.shortcuts import render
#
# from .forms import NameForm
#
# def get_name(request):
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('remove_system/')
#
#     else:
#         form = NameForm()
#
#     return render(request, 'home.html', {'form': form})