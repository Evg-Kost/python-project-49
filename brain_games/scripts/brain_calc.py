from brain_games.cli import welcome_user
from brain_games.games.calc_games import calc_games
from brain_games.module import greet


def main():
    greet()
    calc_games(welcome_user())


if __name__ == "__main__":
    main()
