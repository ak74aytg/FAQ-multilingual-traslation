from django.db import models
from django.core.cache import cache
from ckeditor.fields import RichTextField
from googletrans import Translator
from bs4 import BeautifulSoup


class FAQ(models.Model):

    question = models.TextField(verbose_name="Question (English)")
    answer = RichTextField(verbose_name="Answer (English)", null=True, blank=True)

    question_hi = models.TextField(verbose_name="Question (Hindi)", blank=True, null=True)
    answer_hi = RichTextField(verbose_name="Answer (Hindi)", blank=True, null=True)
    question_bn = models.TextField(verbose_name="Question (Bengali)", blank=True, null=True)
    answer_bn = RichTextField(verbose_name="Answer (Bengali)", blank=True, null=True)

    def __str__(self):
        return self.question

    def translate_text(self, text, dest_lang):
        try:
            if not text:
                return ""

            translator = Translator()
            translation = translator.translate(text, dest=dest_lang)
            return translation.text
        except Exception as e:
            print(f"Translation failed: {e}")
            return text

    def translate_html_content(self, html_text, dest_lang):
        if not html_text:
            return ""

        soup = BeautifulSoup(html_text, "html.parser")

        for element in soup.find_all(text=True):
            translated_text = self.translate_text(element.strip(), dest_lang)
            element.replace_with(translated_text)

        return str(soup)

    def save(self, *args, **kwargs):

        if self.pk:
            old_faq = FAQ.objects.get(pk=self.pk)
            if self.question != old_faq.question:
                self.question_hi = self.translate_text(self.question, 'hi')
                self.question_bn = self.translate_text(self.question, 'bn')
            if self.answer and self.answer != old_faq.answer:
                self.answer_hi = self.translate_html_content(self.answer, 'hi')
                self.answer_bn = self.translate_html_content(self.answer, 'bn')
        else:
            if not self.question_hi:
                self.question_hi = self.translate_text(self.question, 'hi')
            if not self.question_bn:
                self.question_bn = self.translate_text(self.question, 'bn')

            if self.answer and not self.answer_hi:
                self.answer_hi = self.translate_html_content(self.answer, 'hi')
            if self.answer and not self.answer_bn:
                self.answer_bn = self.translate_html_content(self.answer, 'bn')

        super().save(*args, **kwargs)
        self.clear_cache()

    def delete(self, *args, **kwargs):
        self.clear_cache()
        super().delete(*args, **kwargs)

    def get_translated_question(self, lang='en'):
        if lang == 'hi' and self.question_hi:
            return self.question_hi
        elif lang == 'bn' and self.question_bn:
            return self.question_bn
        else:
            return self.question

    def get_translated_answer(self, lang='en'):
        if lang == 'hi' and self.answer_hi:
            return self.answer_hi
        elif lang == 'bn' and self.answer_bn:
            return self.answer_bn
        else:
            return self.answer

    def clear_cache(self):
        languages = ['en', 'hi', 'bn']
        for lang in languages:
            cache_key = f'faqs_{lang}'
            cache.delete(cache_key)
        print("Cache cleared for all languages.")
