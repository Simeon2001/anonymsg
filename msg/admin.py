from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Comment)
class commentAdmin(admin.ModelAdmin):
    list_display = ('post', 'text', 'date_created')
    list_filter = ('post', 'date_created')
    search_fields = ('text','date_created')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'nickname', 'date_created')
    list_filter = ('date_created','nickname')
    search_fields = ('text','date_created')