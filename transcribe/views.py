from django.views.generic import DetailView, ListView

from .models import Text
from .forms import TranscribeForm


class TextView(DetailView):
    model = Text
    template_name = 'transcribe/text_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TranscribeForm
        return context

    def post(self, request, *args, **kwargs):
        form = TranscribeForm(request.POST)
        # Courtesy of https://stackoverflow.com/questions/32497740/
        if form.is_valid():
            self.object = self.get_object()
            context = self.get_context_data()
            return self.render_to_response(context=context)
        else:
            self.object = self.get_object()
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context=context)


class LandingView(ListView):
    model = Text
    template_name = 'transcribe/landing.html'
