from django.contrib import admin
from django.utils.html import format_html
from . import models

class PostAdmin(admin.ModelAdmin):
    list_filter = ['category','brand','type_post','state']
    search_fields = ['title', 'user','state']
    list_display = ['title','user','create_date','state']
class ReportAdmin(admin.ModelAdmin):
    def image_img(self):
        if self.pic:
            return u'<img src="%s" />' % self.pic.url_125x125
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True
    list_filter = ['type_report','create_date']
    search_fields = ['post.user','create_date']
    list_display = ['post','type_report','create_date']
admin.site.register(models.Brand)
admin.site.register(models.Category)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Image)
admin.site.register(models.ReportPost, ReportAdmin)
# Register your models here.
