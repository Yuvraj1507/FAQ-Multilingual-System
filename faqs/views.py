from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get('lang', 'en')  # Default to English
        cache_key = f"faqs_{lang}"  # Create a cache key based on the language

        # Try to get the cached data first
        cached_faqs = cache.get(cache_key)
        if cached_faqs:
            return Response(cached_faqs, status=status.HTTP_200_OK)

        faqs = FAQ.objects.all()
        
        # Serialize the FAQs
        serializer = FAQSerializer(faqs, many=True)
        
        # Add translated questions
        for idx, faq in enumerate(faqs):
            # Dynamically retrieve the translated question based on the selected language
            translated_question = faq.get_translated_question(lang)
            print(f"FAQ ID: {faq.id}, Translated Question: {translated_question}")  # Debugging line
            serializer.data[idx]['translated_question'] = faq.get_translated_question(lang)
        
        response_data = serializer.data

        # Cache the response data for 1 hour (3600 seconds)
        cache.set(cache_key, response_data, timeout=3600)

        return Response(response_data, status=status.HTTP_200_OK)  # Return serialized data
    
def get_translated_question(self, lang='en'):
    """Returns the translated question based on the selected language."""
    translations = {
        'hi': self.question_hi,
        'bn': self.question_bn
    }

def faq_view(request):
    faqs = FAQ.objects.all()
    lang = request.GET.get('lang', 'en')  # Get the language from request parameters
    return render(request, 'faq.html', {'faqs': [(faq.get_translated_question(lang), faq.answer) for faq in faqs]})

    translated = translations.get(lang, self.question)
    print(f"Getting translated question for {lang}: {translated}")  # Debugging line
    return translated
