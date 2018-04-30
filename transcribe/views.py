import html
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404

from .models import Text
from .forms import TranscribeForm


def text_detail_view(request, slug):
    mytext = get_object_or_404(Text, slug=slug)
    if request.method == 'POST':
        form = TranscribeForm(request.POST)
        if form.is_valid():
            # Replace newlines with <br> tags, and escape all HTML tags.
            clean_text = '<br>'.join(html.escape(form.cleaned_data['text']).splitlines())
            clean_author = html.escape(form.cleaned_data['name'])
            mytext.pendingtranscription_set.create(transcription=clean_text, author=clean_author)
            # Create the pending transcription object.
        # TODO: Handle invalid case.
    else:
        form = TranscribeForm()
    context = {'object': mytext, 'form': form}
    return render(request, 'transcribe/text_detail.html', context)


class LandingView(ListView):
    model = Text
    template_name = 'transcribe/landing.html'
