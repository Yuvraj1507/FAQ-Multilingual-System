# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField
from deep_translator import GoogleTranslator

class FAQ(models.Model):
    title = models.CharField(max_length=255)  # Ensure 'title' is defined
    created_at = models.DateTimeField(auto_now_add=True)
    question = models.CharField(max_length=200)
    answer = models.TextField()
    question_hi = models.CharField(max_length=200, blank=True, null=True)  # Hindi translation
    question_bn = models.CharField(max_length=200, blank=True, null=True)  # Bengali translation

    def get_translated_question(self, lang):
        """Returns the translated question if available; otherwise, falls back to English."""
        translations = {
            'hi': self.question_hi,
            'bn': self.question_bn,
        }
        return translations.get(lang, self.question)
    
    def save(self, *args, **kwargs):
        # Translate question to Hindi and Bengali on save
        if not self.question_hi:
            self.question_hi = self.translate_text(self.question, 'hi')
        if not self.question_bn:
            self.question_bn = self.translate_text(self.question, 'bn')
        super().save(*args, **kwargs)
    
    def translate_text(self, text, lang):
        """Translates the provided text to the specified language."""
        translation = GoogleTranslator(source='auto', target=lang).translate(text)
        return translation
    
    def __str__(self):
        return self.question[:50]