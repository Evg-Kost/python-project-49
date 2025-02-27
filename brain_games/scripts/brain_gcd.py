from brain_games.cli import welcome_user
from brain_games.games.gcd_games import gcd_games
from brain_games.module import greet


def main():
    greet()
    gcd_games(welcome_user())


if __name__ == "__main__":
    main()