from GameExchangeSite.GameExchange.models import Game


class GameService:

    def get_all_games_for_platform(self, platform_id):
        return Game.objects.filter(platform__id=platform_id)
