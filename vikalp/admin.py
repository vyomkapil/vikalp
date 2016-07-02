from django.contrib import admin

# Register your models here.
from .models import Company, UserProfile, Branch, Message

admin.site.register(UserProfile)
admin.site.register(Branch)
admin.site.register(Company)
admin.site.register(Message)