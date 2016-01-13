from django.contrib import admin

# Register your models here.
from .models import Company, UserProfile, Branch

class CompanyInLine(admin.StackedInline):
    model = Company

class BranchAdmin(admin.ModelAdmin):
    inlines = [CompanyInLine]

admin.site.register(UserProfile)
admin.site.register(Branch, BranchAdmin)