from rest_framework import serializers
from .models import Library

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'

class CheckoutSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()
