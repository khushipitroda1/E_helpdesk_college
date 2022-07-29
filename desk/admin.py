from django.contrib import admin
from .models import *


# Register your models here.

class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['std_id', 'feed', 'happy', 'sad']


class CollegeAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'city', 'pin_code']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['enroll_no', 'name', 'clg_id', 'gender', 'field', 'semester']


class ComplainAdmin(admin.ModelAdmin):
    list_display = ['std_id', 'type', 'date']

admin.site.register(User)
admin.site.register(College, CollegeAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Complain, ComplainAdmin)
admin.site.register(Feedback, FeedBackAdmin)
