from brain_games.cli import welcome_user
from brain_games.games.progression_games import progression_games
from brain_games.module import greet


def main():
    greet()
    progression_games(welcome_user())


if __name__ == "__main__":
    main()