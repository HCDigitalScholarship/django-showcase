from django import forms


class TranscribeForm(forms.Form):
    text = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Enter your transcription here.'}))
    name = forms.CharField(label='Name (optional)', required=False, max_length=50)
