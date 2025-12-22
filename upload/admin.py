from django.contrib import admin

from upload.models import Upload


# Register your models here.

@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    pass