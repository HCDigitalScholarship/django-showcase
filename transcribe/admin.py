from django.contrib import admin

from .models import Text, PendingTranscription


admin.site.register(Text)
admin.site.register(PendingTranscription)
