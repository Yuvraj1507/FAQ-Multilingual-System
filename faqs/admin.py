# Register your models here.
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import FAQ

# Custom form for the FAQ model to use CKEditor in Django Admin
class FAQForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditorWidget())  # Use CKEditor widget

    class Meta:
        model = FAQ
        fields = '__all__'  # Include all fields

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    form = FAQForm  # Use the custom form with CKEditor
    list_display = ('question', 'created_at')
    list_display = ('title', 'created_at')
    search_fields = ('question', 'question_hi', 'question_bn')
