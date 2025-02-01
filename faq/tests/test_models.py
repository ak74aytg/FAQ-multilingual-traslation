from django.test import TestCase
from faq.models import FAQ


class FAQModelTests(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a high-level Python web framework.",
            question_hi="Django क्या है?",
            answer_hi="Django एक उच्च-स्तरीय Python वेब फ्रेमवर्क है।",
            question_bn="ডjango কি?",
            answer_bn="ডjango হল একটি উচ্চ-স্তরের Python ওয়েব ফ্রেমওয়ার্ক।"
        )

    def test_faq_creation(self):
        self.assertEqual(self.faq.question, "What is Django?")
        self.assertEqual(self.faq.answer, "Django is a high-level Python web framework.")

    def test_get_translated_question(self):
        self.assertEqual(self.faq.get_translated_question('hi'), "Django क्या है?")
        self.assertEqual(self.faq.get_translated_question('bn'), "ডjango কি?")
        self.assertEqual(self.faq.get_translated_question('en'), "What is Django?")

    def test_get_translated_answer(self):
        self.assertEqual(self.faq.get_translated_answer('hi'), "Django एक उच्च-स्तरीय Python वेब फ्रेमवर्क है।")
        self.assertEqual(self.faq.get_translated_answer('bn'), "ডjango হল একটি উচ্চ-স্তরের Python ওয়েব ফ্রেমওয়ার্ক।")
        self.assertEqual(self.faq.get_translated_answer('en'), "Django is a high-level Python web framework.")
