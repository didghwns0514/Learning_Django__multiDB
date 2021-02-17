from django.contrib import admin

# Register your models here.
from .models import AddOrder, RobotState
admin.site.register(AddOrder)
admin.site.register(RobotState)
