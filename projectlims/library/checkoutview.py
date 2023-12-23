from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Library
from .serializers import CheckoutSerializer
from django.utils import timezone

class CheckoutAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CheckoutSerializer(data=request.data)
        if serializer.is_valid():
            book_id = serializer.validated_data['book_id']
            try:
                book = Library.objects.get(id=book_id)
                if book.is_in_stock:
                    book.date_checked_out = timezone.now()
                    book.is_in_stock = False
                    book.save()
                    response_data = {
                        'success': True,
                        'book_id': book.id,
                        'date_checked_out': book.date_checked_out,
                        'is_in_stock': book.is_in_stock,
                    }
                else:
                    response_data = {
                        'success': False,
                        'message': 'Book is not in stock.',
                    }
            except Library.DoesNotExist:
                response_data = {
                    'success': False,
                    'message': 'Book not found.',
                }
        else:
            response_data = {
                'success': False,
                'message': 'Invalid input.',
            }

        return Response(response_data, status=status.HTTP_200_OK)
