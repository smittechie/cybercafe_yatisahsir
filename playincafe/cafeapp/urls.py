from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import MyLoginView, SystemDetailView, SystemAddView, SystemDeleteView, AddUserView, UserListView, \
    StatusListofSysytems, UpdateUserview, ReleaseView, HistoryListView, AllotmentofSystemsView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TemplateView.as_view(template_name='cafeapp/home.html'), name='home'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('add_system/', SystemAddView.as_view(), name='add_system'),
    path('add_system/system_detail/', SystemDetailView.as_view(), name='system_detail'),
    path('system/<int:pk>/', SystemDeleteView.as_view(), name='remove_system'),
    path('add_user/', AddUserView.as_view(), name='adduser'),
    path('userdetail/', UserListView.as_view(), name='userlist'),
    path('allot_system/', AllotmentofSystemsView.as_view(), name='allotsystem'),
    path('alloted_system_list/', StatusListofSysytems.as_view(), name='sysytemstatuslist'),
    path('update_user_view/<int:pk>/', UpdateUserview.as_view(), name='update_user'),
    path('releasesystem/<int:pk>/', ReleaseView.as_view(), name='releasesystem'),
    path('history_list/', HistoryListView.as_view(), name='history_list'),

]
