# Create your tests here.
from django.test import TestCase
from .models import FAQ
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class FAQModelTest(TestCase):
    
    def test_faq_translation(self):
        faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a high-level Python Web framework."
        )

        # Check if the translations are created
        self.assertEqual(faq.question_hi, "डjango क्या है?")  # Replace with expected Hindi translation
        self.assertEqual(faq.question_bn, "ডjango কি?")      # Replace with expected Bengali translation

    def test_get_translated_question(self):
        faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a high-level Python Web framework."
        )

        # Test the method for getting translated questions
        self.assertEqual(faq.get_translated_question('hi'), "डjango क्या है?")  # Replace with expected Hindi translation
        self.assertEqual(faq.get_translated_question('bn'), "ডjango কি?")      # Replace with expected Bengali translation
        self.assertEqual(faq.get_translated_question('en'), "What is Django?")

class FAQApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        FAQ.objects.create(
            question="What is Django?",
            answer="Django is a high-level Python Web framework."
        )

    def test_get_faqs(self):
        url = reverse('get_faqs')

        # Test for default language (English)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('What is Django?', [faq['question'] for faq in response.data])

        # Test for Hindi language
        response = self.client.get(url + '?lang=hi')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('डjango क्या है?', [faq['question'] for faq in response.data])

        # Test for Bengali language
        response = self.client.get(url + '?lang=bn')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('ডjango কি?', [faq['question'] for faq in response.data])

