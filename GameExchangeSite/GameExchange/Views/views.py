from rest_framework import viewsets
from rest_framework.response import Response

from GameExchangeSite.GameExchange.Services.game_service import GameService
from GameExchangeSite.GameExchange.serializers import GameSerializer, PriceSerializer, PlatformSerializer, UserSerializer, GroupSerializer
from GameExchangeSite.GameExchange.models import Game, Price, Platform
from django.contrib.auth.models import User, Group
from rest_framework import mixins
from rest_framework.decorators import api_view, action


# Create your views here.


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('pk')
    serializer_class = GameSerializer


class PriceViewSet(mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})


class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

    @action(detail=True)
    def games(self, request, pk=None):
        queryset = Response(GameService().get_all_games_for_platform(pk))
        serializer_class = GameSerializer


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
