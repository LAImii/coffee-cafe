from django.contrib import admin
from app_login.models import Register

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    # list_display = ['username', 'password', 'fullname', 'email']
    search_fields = ['username']
    # list_filter = ['xxx']

admin.site.register(Register, RegisterAdmin)