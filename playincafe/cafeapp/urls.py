from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import MyLoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', TemplateView.as_view(template_name='cafeapp/home.html'), name='home'),
    path('login/', MyLoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),

]
