from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Option(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='./options/', blank=True, null=True)


class Question(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='./questions/', blank=True, null=True)
    options = models.ManyToManyField(Option, related_name='options', verbose_name='Options')
    correct_answer = models.ManyToManyField(Option, related_name='correct_answer', verbose_name='Correct answer')
    