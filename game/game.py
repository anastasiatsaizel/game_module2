import random

def roll_dice():
    return random.randint(1, 6)

def play_round(player, computer):
    input("Roll a dice (Enter): ")

    player_roll = roll_dice()
    computer_roll = roll_dice()

    print(f"Player: 🎲 {player_roll}")
    print(f"Computer: 🎲 {computer_roll}")

    if player_roll > computer_roll:
        player.score += (player_roll - computer_roll)

    elif computer_roll > player_roll:
        player.score -= (computer_roll - player_roll)

    elif player_roll == computer_roll:
        print("Draw. Roll again!")
        return play_round(player, computer)