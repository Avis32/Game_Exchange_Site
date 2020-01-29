from rest_framework import serializers, request

from .models import Price, Game, Platform
from django.contrib.auth.models import User, Group


class PriceSerializer(serializers.HyperlinkedModelSerializer):
    percents = serializers.SerializerMethodField('percentage')

    def percentage(self, price):
        return round(price.price * 100/price.base_price, 2)

    class Meta:
        model = Price
        fields = ['game', 'price', 'base_price', 'percents']


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


class GameSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField()
    game_price = serializers.FloatField(write_only=True)
    added_date = serializers.DateField(read_only=True)

    class Meta:
        model = Game
        fields = '__all__'
        read_only_fields = ('price', 'user')

    def create(self, validated_data):
        price = Price.objects.create(price=validated_data.get('game_price'),
                                     base_price=validated_data.get('game_price'))
        validated_data.pop('game_price', None)
        user = self.context['request'].user
        print(user)
        print(validated_data)
        return Game(**validated_data, price=price, user=user)
