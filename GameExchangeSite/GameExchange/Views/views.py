from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response

from GameExchangeSite.GameExchange.serializers import GameSerializer, PriceSerializer, PlatformSerializer, UserSerializer, GroupSerializer
from GameExchangeSite.GameExchange.models import Game, Price, Platform
from django.contrib.auth.models import User, Group
from rest_framework import mixins
from rest_framework.decorators import api_view, action


# Create your views here.


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('pk')
    serializer_class = GameSerializer


class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

    @action(detail=True, methods=['GET'])
    def games(self, request, pk):
        queryset = Game.objects.filter(platform=pk)
        serializer = GameSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
