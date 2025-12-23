from celery import Celery
from upload.models import Upload

app = Celery('tasks', broker='redis://127.0.0.1')

@app.task
def check_paper(upload_uuid):
    upload = Upload.objects.filter(uuid=upload_uuid).first()
    if upload:
        print(f"processing {upload.uuid}")