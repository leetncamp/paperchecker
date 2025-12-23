from django.contrib import admin
from paperchecker.tasks import check_paper
from upload.models import Upload


# Register your models here.

@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):

    def delete_and_remove_upload(self, request, queryset):
        for obj in queryset:
            obj.upload_paper.delete(False)
            obj.delete()

    def process(self, request, queryset):
        for instance in queryset:
            check_paper.delay(instance.uuid)
    process.short_description = "Check Paper"
    actions = [process, delete_and_remove_upload]

    actions = ['delete_and_remove_upload', 'process']