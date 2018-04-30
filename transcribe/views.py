import difflib
import html
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import Text, PendingTranscription
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


class ReviewTranscriptionList(ListView):
    model = PendingTranscription
    template_name = 'transcribe/review_transcription_list.html'


def review_transcription(request, pk):
    """A view on the admin page to appprove or delete pending transcriptions."""
    obj = get_object_or_404(PendingTranscription, pk=pk)
    if request.method == 'POST':
        if 'deletebutton' in request.POST:
            obj.delete()
            messages.success(request, 'The transcription was successfully deleted.')
        else:
            if obj.doc.transcription:
                obj.doc.backup_transcription = obj.doc.transcription
            obj.doc.transcription = obj.transcription
            obj.doc.save()
            obj.delete()
            messages.success(request, 'The transcription was successfully approved.')
        return HttpResponseRedirect('/admin')
    else:
        # The transcription is line-delineated by <br> tags instead of newlines, but difflib can
        # only generate diffs for newline-delineated strings.
        old_lines = split_html_lines(obj.doc.transcription)
        new_lines = split_html_lines(obj.transcription)
        d = difflib.Differ()
        diff_lines = list(d.compare(old_lines, new_lines))
        for i, line in enumerate(diff_lines):
            if line.startswith('  '):
                diff_lines[i] = '<span class="diff-both">' + line[2:] + '</span>'
            elif line.startswith('- '):
                diff_lines[i] = '<span class="diff-first">' + line[2:] + '</span>'
            elif line.startswith('+ '):
                diff_lines[i] = '<span class="diff-second">' + line[2:] + '</span>'
            elif line.startswith('? '):
                diff_lines[i] = '<span class="diff-neither">' + line[2:] + '</span>'
        context = {
            'object': obj,
            'diff_table': '<br>'.join(diff_lines)
        }
        return render(request, 'transcribe/review_transcription.html', context)


def split_html_lines(html_str):
    return html_str.split('<br>')
