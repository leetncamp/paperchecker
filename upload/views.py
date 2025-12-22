from django import forms
from django.shortcuts import render
from django.utils.safestring import mark_safe

from .models import Upload


class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        exclude = []
        labels = {
            'confirm_exactly_as_in_openreview': mark_safe('I confirm the information below is '
                                                          '<strong>exactly</strong> as in OpenReview'),
            'confirm_styles': 'I confirm that the paper is compiled with the latest version of the ICML 2025 style '
                              'files (from here), and I have not modified this style file.',
            'confirm_title': "I confirm that my camera-ready PDF lists the correct title and authors on the first "
                             "page, and the correct running title at the top of subsequent pages (which is not blank "
                             "and does not say 'Submission and Formatting Instructions for ICML 2025')",
            'confirm_9_pages': 'I confirm that the main body of the paper is no more than 9 pages (excluding '
                               'acknowledgments, impact statement, and references)',
            'confirm_appendices': 'I confirm that the appendices of the paper are included in the paper pdf file but '
                                  'not a part of the supplementary zip file',
            'confirm_abstract': 'I confirm that my abstract is one paragraph, and ideally 4-6 sentences',
            'confirm_title_case': 'I confirm that my title and section headings are "In the Title Case Format" and '
                                  'not "ALL CAPS"',
            'confirm_macos_preview': 'I confirm that I have not used MacOS Preview to process the paper or any other '
                                     'package that might alter the margins',
            'confirm_type_3_fonts': 'I understand that there is no Type 3 font check, and I confirm that I have not '
                                    'converted eps figures to png figures just to bypass the check',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def clean_confirm_exactly_as_in_openreview(self):
            data = self.cleaned_data["confirm_exactly_as_in_openreview"]
            if not data:
                raise forms.ValidationError("Please confirm.")

        def clean_confirm_styles(self):
            data = self.cleaned_data["confirm_styles"]
            if not data:
                raise forms.ValidationError("Please confirm.")

        def clean_confirm_title(self):
            data = self.cleaned_data["confirm_title"]
            if not data:
                raise forms.ValidationError("Please confirm.")

        def clean_confirm_9_pages(self):
            data = self.cleaned_data["confirm_9_pages"]
            if not data:
                raise forms.ValidationError("Please confirm.")

        def clean_confirm_appendices(self):
            data = self.cleaned_data["confirm_appendices"]
            if not data:
                raise forms.ValidationError("Please confirm.")

        def clean_confirm_abstract(self):
            data = self.cleaned_data["confirm_abstract"]
            if not data:
                raise forms.ValidationError("Please confirm.")

        def clean_confirm_title_case(self):
            data = self.cleaned_data["confirm_title_case"]
            if not data:
                raise forms.ValidationError("Please confirm.")

        def clean_confirm_macos_preview(self):
            data = self.cleaned_data["confirm_macos_preview"]
            if not data:
                raise forms.ValidationError("Please confirm.")

        def clean_confirm_type_3_fonts(self):
            data = self.cleaned_data["confirm_type_3_fonts"]
            if not data:
                raise forms.ValidationError("Please confirm.")


def upload(request):
    if request.method == 'POST':
        uploadForm = UploadForm(request.POST, request.FILES)
        if uploadForm.is_valid():
            pass
        else:
            pass
    else:
        uploadForm = UploadForm()
    return render(request, 'upload/upload.html', locals())