from django.contrib import admin
from django.utils.html import format_html
from . import models


def make_open(modeladmin, request, queryset):
    queryset.update(state='open')
make_open.short_description = "Mark selected stories as open"
def make_close(modeladmin, request, queryset):
    queryset.update(state='close')
make_close.short_description = "Mark selected stories as close"

class PostAdmin(admin.ModelAdmin):
    list_filter = ['category','brand','type_post','state']
    search_fields = ['title', 'user__username']
    list_display = ['title','user','create_date','state']
    list_editable = ['state']
    actions = [make_open,make_close]
    list_per_page = 10

class ReportAdmin(admin.ModelAdmin):
    def show_user(self, obj):
        return format_html("<a href='{url}'>"+str(obj.post.user)+"</a>", url='/users/profile/'+str(obj.post.user.id))

    show_user.short_description = "Người đăng"
    def show_post(self, obj):
        return format_html("<a href='{url}'>"+str(obj.post.title)+"</a>", url='/post/'+str(obj.post.id))

    show_post.short_description = "Link bài viết"
    def image_img(self,obj):
        return format_html('<img src="{url}" style="width:125px;height:125px;">', url=obj.pic.url)
    image_img.short_description = 'Hình ảnh'
    image_img.allow_tags = True

    list_filter = ['type_report','create_date']
    search_fields = ['post__user__username','create_date']
    list_display = ['post','image_img','type_report','create_date','show_post','show_user']
    list_display_links = ['post']
    readonly_fields = ['post','content','image_img','type_report','create_date']
    list_per_page = 10
admin.site.register(models.Brand)
admin.site.register(models.Category)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Image)
admin.site.register(models.ReportPost, ReportAdmin)
# Register your models here.
