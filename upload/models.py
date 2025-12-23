import uuid
from django.db import models
from django.core.exceptions import ValidationError
from pypdf import PdfReader
from django.utils.translation import gettext_lazy as _


MAX_PDF_MB = 20
MAX_PDF_BYTES = MAX_PDF_MB * 1024 * 1024
PDF_MAGIC = b"%PDF-"


def validate_pdf_20mb(file_obj) -> None:
    """
    Combined validator:
    - max size <= 20 MB
    - actual PDF header starts with b'%PDF-'
    - parseable as a PDF via pypdf (structural validation)

    Works with Django UploadedFile / File objects.
    """
    # 1) Size check (fast)
    size = getattr(file_obj, "size", None)
    if size is not None and size > MAX_PDF_BYTES:
        raise ValidationError(_(f"File must be {MAX_PDF_MB} MB or less."))

    # 2) Magic header check (fast)
    try:
        file_obj.seek(0)
        head = file_obj.read(len(PDF_MAGIC))
        file_obj.seek(0)
    except Exception:
        raise ValidationError(_("Could not read uploaded file."))

    if head != PDF_MAGIC:
        raise ValidationError(_("File is not a valid PDF (missing %PDF- header)."))

    # 3) Structural validation (heavier)
    try:
        # PdfReader reads from the stream; do not trust client MIME/extension.
        reader = PdfReader(file_obj, strict=False)
        # Touch at least one property to force parsing work.
        _ = len(reader.pages)
    except Exception:
        raise ValidationError(_("File appears to be a corrupted or invalid PDF."))
    finally:
        # Always rewind so later processing/saving works correctly.
        try:
            file_obj.seek(0)
        except Exception:
            pass


class Upload(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    confirm_exactly_as_in_openreview = models.BooleanField(default=False)
    paper_id = models.IntegerField(blank=False, null=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    upload_paper = models.FileField(
        upload_to='uploads/', validators=[validate_pdf_20mb])
    type = models.CharField(choices=[('Paper', 'Paper'), ('Position Paper', 'Position Paper')])
    confirm_styles = models.BooleanField(default=False)
    confirm_title = models.BooleanField(default=False)
    confirm_9_pages = models.BooleanField(default=False)
    confirm_appendices = models.BooleanField(default=False)
    confirm_abstract = models.BooleanField(default=False)
    confirm_title_case = models.BooleanField(default=False)
    confirm_macos_preview = models.BooleanField(default=False)
    confirm_type_3_fonts = models.BooleanField(default=False)


    def __str__(self):
        return self.upload_paper.name

