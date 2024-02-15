from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Option(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='./options/', blank=True, null=True)

