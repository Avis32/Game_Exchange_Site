from rest_framework import serializers

from .models import Price, Game, Platform
from django.contrib.auth.models import User, Group


class GameSerializer(serializers.HyperlinkedModelSerializer):
    #price = serializers.FloatField()
    #name = serializers.StringRelatedField()
    price_to_set = serializers.FloatField(allow_null=True, write_only=True, label='price', required=True)
    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ('user', 'price')

    def create(self, validated_data):
        pass


class PriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platform
        read_only_fields = ['games', ]
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']
        read_only_fields = ('email',)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
