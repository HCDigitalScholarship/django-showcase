from django.db import models
from django.utils.text import slugify


class Text(models.Model):
    title = models.CharField(max_length=100)
    # A slug is a text field that can be displayed in a URL: it is just the
    # title, in lowercase and with dashes instead of spaces.
    slug = models.SlugField()
    transcription = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        # We want to make sure the slug is set to the title every time we save
        # the document.
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
