from brain_games.cli import welcome_user
from brain_games.games.even_games import even_game
from brain_games.module import greet


def main():
    greet()
    even_game(welcome_user())


if __name__ == "__main__":
    main()