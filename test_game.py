from game.models import Player
from game.settings import GAME_LEVELS

def test_player_creation():
    player = Player("Nastya")

    assert player.name == "Nastya"
    assert player.score == 0
# проверяю что имя сохраняется и начальный score 0

def test_game_levels():
    assert GAME_LEVELS["1"] == 5
    assert GAME_LEVELS["2"] == 8
    assert GAME_LEVELS["3"] == 10
# проверяю что количество ходов соответствует уровню