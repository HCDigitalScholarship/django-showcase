from django.views.generic import DetailView, ListView

from .models import Text


class TextView(DetailView):
    model = Text
    template_name = 'transcribe/text_detail.html'


class LandingView(ListView):
    model = Text
    template_name = 'transcribe/landing.html'
