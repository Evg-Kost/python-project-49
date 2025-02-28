from brain_games.cli import welcome_user
from brain_games.games.prime_games import prime_games
from brain_games.module import greet


def main():
    greet()
    prime_games(welcome_user())


if __name__ == "__main__":
    main()
