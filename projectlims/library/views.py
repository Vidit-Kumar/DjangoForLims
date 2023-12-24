from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from faker import Faker
from .models import Library
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
import random
import sys
from django.contrib.auth.models import User
# Create your views here.

class BookView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
   
    
    def get_queryset(self):
        queryset = Library.objects.all()
        limit = self.request.query_params.get('limit', None)
        if limit is not None:
            try:
                limit = int(limit)
                queryset = queryset[:limit]
            except ValueError:
                pass
        return queryset

    @action(detail=True, methods=['post'])
    def checkout(self, request, pk=None):
        book = self.get_object()

        if book.is_in_stock:
            book.date_checked_out = timezone.now()
            book.is_in_stock = False
            book.save()
            serializer = self.get_serializer(book)
            return Response({'success': True, 'data': serializer.data})
        else:
            return Response({'success': False, 'message': 'Book is not in stock.'})



def library(request):
  # get_template look for templates folder and in there look for 
  # given html file for render.
  template = loader.get_template('library.html')
  return HttpResponse(template.render())


fake = Faker()

def populate_library_data():
    if  'makemigrations' in sys.argv or 'migrate' in sys.argv: 
        return 
    if Library.objects.count() == 0:
        for _ in range(200):
            Library.objects.create(
                publisher=fake.company(),
                author=fake.name(),
                title=fake.catch_phrase(),
                page_count=random.randint(50, 500),
                category=fake.word(),
                shelf_location=fake.random_element(elements=('A1', 'B2', 'C3')),
                published_date=fake.date_between(start_date='-5y', end_date='today'),
                is_in_stock=random.choice([True, False]),
                date_checked_out=fake.date_between(start_date='-1y', end_date='today') if random.choice([True, False]) else None,
            )



def books(request):
    libraries = Library.objects.all()
    return render(request, 'books.html', {'libraries': libraries})

def admin_page(request):
    users = User.objects.all()
    return render(request, 'adminview.html', {'users': users})

populate_library_data()


