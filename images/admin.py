from django.contrib import admin

from images import models


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image', 'created',)
    list_filter = ('created',)
