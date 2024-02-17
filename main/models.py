from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Option(models.Model):
    """Question options"""
    title = RichTextUploadingField(verbose_name='Title')
    image = models.ImageField(upload_to='./options/', blank=True, null=True)

    def __str__(self):
        return f"{self.title}"


class Question(models.Model):
    """Credit questions"""
    title = RichTextUploadingField(verbose_name='Title')
    image = models.ImageField(upload_to='./questions/', blank=True, null=True)
    options = models.ManyToManyField(Option, related_name='options', verbose_name='Options', blank=True)
    corrects = models.ManyToManyField(Option, related_name='corrects', verbose_name='Correct answer', blank=True)
    description = RichTextUploadingField(verbose_name="Description", blank=True, null=True)

    def __str__(self):
        return f"{self.title}"


class CreditQuestion(models.Model):
    """Test of the Credit."""
    title = models.CharField(max_length=255, verbose_name='Title')
    description = RichTextUploadingField(verbose_name='Description')
    code = models.CharField(max_length=20, verbose_name='code', help_text="")
    questions = models.ManyToManyField(Question, related_name='questions', verbose_name='Question', blank=True)

    def __str__(self):
        return f"{self.code} - {self.title}"

