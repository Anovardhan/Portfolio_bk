

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(MyInfo)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Certification)