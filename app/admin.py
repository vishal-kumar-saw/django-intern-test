from django.contrib import admin
from .models import *
from django.utils.html import format_html


# Register your models here.

admin.site.site_header = "Intern Assignment"
admin.site.site_title = "Intern Assignment"
admin.site.index_title = "Welcome to Food Admin Panel"





# admin.site.register(KidTable)
# admin.site.register(ImageTable)


@admin.register(KidTable) 
class KidTableAdmin(admin.ModelAdmin):
    fields = ['name', 'age', 'phone', 'email']
    list_display = ('name', 'age', 'phone', 'email')
    


@admin.register(ImageTable) 
class ImageTableAdmin(admin.ModelAdmin):
    fields = ['kid', 'image_url', 'image_tag', 'created_on', 'updated_on', 'approved_by', 'Food_group']
    readonly_fields = ['image_tag', 'updated_on']
    radio_fields = {"Food_group": admin.HORIZONTAL}
    list_display = ('image_url', 'image_tag', 'created_on', 'updated_on', 'is_approved', 'approved_by', 'Food_group')
    
     


