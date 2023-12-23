from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import BookView
from .checkoutview import CheckoutAPIView
router = DefaultRouter()
router.register(r'books', BookView, basename='bookview')
#router.register(r'checkoutviews', CheckoutAPIView, basename='checkoutapiview')

urlpatterns = [
    path('', views.library, name='library'),
    path('books/', views.books, name='books'),
    path('adminview/', views.admin_page, name='adminview'),   
    path('api/', include(router.urls)), 
    path('api/checkout/', CheckoutAPIView.as_view(), name='checkout_api'),   
   
]
