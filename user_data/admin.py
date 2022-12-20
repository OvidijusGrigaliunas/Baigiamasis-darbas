from django.contrib import admin

from .models import User_Data, Record, Category

admin.site.register(User_Data)
admin.site.register(Record)
admin.site.register(Category)