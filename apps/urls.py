from django.urls import path
from .views import StockPriceListAPIView

urlpatterns = [
    path('stocks/', StockPriceListAPIView.as_view(), name='stock-list'),
]