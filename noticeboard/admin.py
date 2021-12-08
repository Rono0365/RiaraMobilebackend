from django.contrib import admin
from noticeboard.models import Post
from students.models import Student
from students.models import Unit
from students.models import Course
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']
admin.site.register(Post)
admin.site.register(Student)
admin.site.register(Unit)
admin.site.register(Course)