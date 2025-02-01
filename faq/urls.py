from django.urls import path
from .views import FAQView

urlpatterns = [
    path('faqs/', FAQView.as_view(), name='all_faqs'),
    path('faqs/<int:faq_id>/', FAQView.as_view(), name='faq_detail'),
]
