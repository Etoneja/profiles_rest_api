from django.contrib import admin

# Register your models here.
from profiles_api.models import UserProfile


admin.site.register(UserProfile)

