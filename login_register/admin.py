from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import User
from . import models

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','is_active')
    list_filter = ('is_staff', 'is_superuser','is_active')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    def show_user(self, obj):
        return format_html("<a href='{url}'>"+str(obj.user.username)+"</a>", url='/admin/auth/user/'+str(obj.user.id))
    def show_profile(self, obj):
        return format_html("<a href='{url}'>"+str(obj.user.email)+"</a>", url='/users/profile/'+str(obj.user.id))

    def image_img(self,obj):
        return format_html('<img src="{url}" style="width:125px;height:125px;">', url=obj.pic.url)
    image_img.short_description = 'Hình ảnh'
    image_img.allow_tags = True

    show_profile.short_description = "Link người dùng"
    readonly_fields = ('user',)
    search_fields = ['user__username']
    list_filter = ['user__date_joined','user__is_active']
    list_display = ['show_user','image_img','show_profile','phone']
    
admin.site.register(models.Profile,ProfileAdmin)