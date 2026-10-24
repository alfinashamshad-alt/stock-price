from django.shortcuts import render
from rest_framework import generics
from .models import StockPrice
from .serializers import StockPriceSerializer


def home(request):
    return render(request, 'app/home.html')


def dashboard(request):
    return render(request, 'app/dashboard.html')


class StockPriceListAPIView(generics.ListCreateAPIView):
    queryset = StockPrice.objects.all()
    serializer_class = StockPriceSerializer