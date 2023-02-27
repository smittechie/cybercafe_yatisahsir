from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import MyLoginView, SystemDetailView, SystemAddView, SystemDeleteView, AddUserView, UserListView, \
    StatusofSysytems
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TemplateView.as_view(template_name='cafeapp/home.html'), name='home'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('add_system/', SystemAddView.as_view(), name='add_system'),
    path('add_system/system_detail/', SystemDetailView.as_view(), name='system_detail'),
    path('system/<int:pk>', SystemDeleteView.as_view(), name='remove_system'),
    path('add_user/', AddUserView.as_view(), name='adduser'),
    path('userdetail/', UserListView.as_view(), name='userlist'),
    path('status/', StatusofSysytems.as_view(), name='sysytemstatus'),

]
