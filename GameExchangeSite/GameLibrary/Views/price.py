from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response

from GameExchangeSite.GameLibrary.serializers import GameSerializer, PriceSerializer, PlatformSerializer, UserSerializer, GroupSerializer
from GameExchangeSite.GameLibrary.models import Game, Price, Platform
from django.contrib.auth.models import User, Group
from rest_framework import mixins
from rest_framework.decorators import api_view, action


class PriceViewSet(mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

    @action(methods=['GET'], detail=True)
    def price_percentage(self, request, pk):
        price = Price.objects.get(pk=pk)
        base_price = price.base_price
        price_set = price.price
        result = price_set*100/base_price
        return Response({'percentage': result})
