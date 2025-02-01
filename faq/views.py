from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import FAQ
from .serializers import FAQSerializer


class FAQView(APIView):
    def get(self, request, faq_id=None):
        lang = request.query_params.get('lang', 'en')

        if faq_id:
            faq = get_object_or_404(FAQ, id=faq_id)
            data = {
                'id': faq.id,
                'question': faq.get_translated_question(lang),
                'answer': faq.get_translated_answer(lang),
            }
            return Response(data, status=status.HTTP_200_OK)

        cache_key = f'faqs_{lang}'
        cached_response = cache.get(cache_key)
        if cached_response:
            print("chached response: ", cached_response)
            return Response(cached_response, status=status.HTTP_200_OK)

        faqs = FAQ.objects.all()
        # data = [{'id': faq.id, 'question': faq.get_translated_question(lang), 'answer': faq.get_translated_answer(lang)} for faq in faqs]
        data = []
        for faq in faqs:
            res = {
                'id': faq.id,
                'question': faq.get_translated_question(lang),
                'answer': faq.get_translated_answer(lang),
            }
            data.append(res)

        cache.set(cache_key, data, timeout=60 * 15)
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = FAQSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete_pattern('faqs_*')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, faq_id):
        faq = get_object_or_404(FAQ, id=faq_id)
        serializer = FAQSerializer(faq, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            cache.delete_pattern('faqs_*')
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, faq_id):
        faq = get_object_or_404(FAQ, id=faq_id)
        faq.delete()
        cache.delete_pattern('faqs_*')
        return Response({'message': 'FAQ deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
