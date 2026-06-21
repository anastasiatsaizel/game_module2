from game.game import play_round
from game.models import Player, Computer
from game.settings import GAME_LEVELS
from game.score import save_result, get_results


def main():
    while True:
        print("\n1 - Play")
        print("2 - See results")
        print("3 - Quit\n")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Enter your name: ")
            player = Player(name)
            computer = Computer()

            print("Choose level:")
            print("1 - Short (5)")
            print("2 - Medium (8)")
            print("3 - Long (10)")

            level = input("Enter your level: ")
            rounds = GAME_LEVELS.get(level)

            if not rounds:
                print("Incorrect input")
                continue

            for _ in range(rounds):
                play_round(player, computer)

            print("\nRound result:")
            print("Player:", player.name)
            print("Score:", player.score)

            save_result(player.name, rounds, player.score)

        elif choice == "2":
            get_results()

        elif choice == "3":
            print("See you soon!")
            break

        else:
            print("Invalid input")


main()