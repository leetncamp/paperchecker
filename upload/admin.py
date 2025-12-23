from django.contrib import admin

from upload.models import Upload


# Register your models here.

@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):

    def delete_and_remove_upload(self, request, queryset):
        for obj in queryset:
            obj.upload_paper.delete(False)
            obj.delete()

    actions = ['delete_and_remove_upload']