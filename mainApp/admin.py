from django.contrib import admin
from .models import News,RegisterData


@admin.register(RegisterData)
class RegisterDataAdmin(admin.ModelAdmin):
    list_display  =['first_name','last_name','phone_number','state']
    list_filter =('state','local_govt','sex')

    # search_fields = ['name']

admin.site.register(News)