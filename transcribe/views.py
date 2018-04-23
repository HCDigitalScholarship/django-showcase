from django.views.generic import DetailView

from .models import Text


class TextView(DetailView):
    model = Text
    template_name = 'transcribe/text_detail.html'
