from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Text(models.Model):
    title = models.CharField(max_length=100)
    # A slug is a text field that can be displayed in a URL: it is just the
    # title, in lowercase and with dashes instead of spaces.
    slug = models.SlugField()
    transcription = models.TextField(blank=True)
    backup_transcription = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        # We want to make sure the slug is set to the title every time we save
        # the document.
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('transcribe:text_detail', args=[self.slug])

    def __str__(self):
        return self.title


class PendingTranscription(models.Model):
    """A model for transcriptions that have been submitted but not yet approved."""
    transcription = models.TextField()
    author = models.CharField(max_length=50, blank=True)
    uploaded = models.DateTimeField(auto_now_add=True)
    doc = models.ForeignKey(Text, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('admin_review_transcription', args=[self.pk])

    def __str__(self):
        if self.author:
            return 'Pending Transcription of {0.doc.title} by {0.author}'.format(self)
        else:
            return 'Pending Transcription of {0.doc.title}'.format(self)
