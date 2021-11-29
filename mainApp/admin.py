from django.contrib import admin
from .models import ( News,RegisterData,User,BlogPosts,BlogContent)


@admin.register(RegisterData)
class RegisterDataAdmin(admin.ModelAdmin):
    list_display  =['first_name','last_name','phone_number','state']
    list_filter =('state','local_govt','sex')

    # search_fields = ['name']

admin.site.register(News)




class BlogContents(admin.TabularInline):
    model =BlogContent
    extra=1

class BlogPostAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['is_approved','title','author','main_image']})]
    inlines=[BlogContents]


admin.site.register(BlogPosts,BlogPostAdmin)