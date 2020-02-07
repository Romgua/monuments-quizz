from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import QuizzUser
from .models import Monument

admin.site.register(QuizzUser)
admin.site.register(Monument)