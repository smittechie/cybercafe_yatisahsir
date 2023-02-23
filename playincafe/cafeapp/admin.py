from django.contrib import admin

from .models import History, Status, System, User

# Register your models here.
admin.site.register(User),
admin.site.register(System),
admin.site.register(Status),
admin.site.register(History),