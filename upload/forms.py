from django import forms




class UploadForm(forms.ModelForm):
    class Meta:
        model = "Upload"
        exclude = []
        labels = {
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
