from rest_framework import serializers
from .models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

    def validate(self, data):
        if not data.get("question"):
            raise serializers.ValidationError({"question": "This field is required."})
        return data
