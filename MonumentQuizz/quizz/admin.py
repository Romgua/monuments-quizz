from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import QuizzUser
from .models import Monument
from .models import UserMonument

admin.site.register(QuizzUser)
admin.site.register(Monument)
admin.site.register(UserMonument)