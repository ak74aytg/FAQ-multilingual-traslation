from django.urls import reverse
from rest_framework.test import APITestCase
from faq.models import FAQ


class FAQViewTests(APITestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a high-level Python web framework.",
            question_hi="Django क्या है?",
            answer_hi="Django एक उच्च-स्तरीय Python वेब फ्रेमवर्क है।",
            question_bn="ডjango কি?",
            answer_bn="ডjango হল একটি উচ্চ-স্তরের Python ওয়েব ফ্রেমওয়ার্ক।"
        )

    def test_get_faqs_in_english(self):
        """Test fetching FAQs in English."""
        url = reverse('all_faqs')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['question'], "What is Django?")
        self.assertEqual(response.data[0]['answer'], "Django is a high-level Python web framework.")

    def test_get_faqs_in_hindi(self):
        """Test fetching FAQs in Hindi."""
        url = reverse('all_faqs') + '?lang=hi'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['question'], "Django क्या है?")
        self.assertEqual(response.data[0]['answer'], "Django एक उच्च-स्तरीय Python वेब फ्रेमवर्क है।")

    def test_get_faqs_in_bengali(self):
        url = reverse('all_faqs') + '?lang=bn'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['question'], "ডjango কি?")
        self.assertEqual(response.data[0]['answer'], "ডjango হল একটি উচ্চ-স্তরের Python ওয়েব ফ্রেমওয়ার্ক।")
