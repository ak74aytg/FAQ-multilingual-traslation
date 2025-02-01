from django.contrib import admin
from django.utils.html import strip_tags
from .models import FAQ


class FAQAdmin(admin.ModelAdmin):
    list_display = ("id", "get_question_text", "get_question_hi", "get_question_bn")

    def get_question_text(self, obj):
        return strip_tags(obj.question)

    def get_question_hi(self, obj):
        return strip_tags(obj.question_hi) if obj.question_hi else "-"

    def get_question_bn(self, obj):
        return strip_tags(obj.question_bn) if obj.question_bn else "-"

    get_question_text.short_description = "QUESTION (ENGLISH)"
    get_question_hi.short_description = "QUESTION (HINDI)"
    get_question_bn.short_description = "QUESTION (BENGALI)"

    fields = ("question", "question_hi", "question_bn", "answer", "answer_bn", "answer_hi")


admin.site.register(FAQ, FAQAdmin)
