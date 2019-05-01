from django.contrib import admin

from . models import Shift
from . models import StaffMember

# Register your models here.
admin.site.register(Shift)
admin.site.register(StaffMember)
