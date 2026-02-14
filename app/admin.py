from django.contrib import admin

# Register your models here.
from . models import Course

class courseadmin(admin.ModelAdmin):
    list_display = ['id','cname','cdur','cprice']
admin.site.register(Course,courseadmin)
admin.site.site_title = "Course"
admin.site.site_header = "Sudheer Admin Panel"

# For Student Database
from . models import student

class studentadmin(admin.ModelAdmin):
    list_display = ['id' ,'name', 'email']
admin.site.register(student,studentadmin)

