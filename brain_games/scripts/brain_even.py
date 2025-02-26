import random
from brain_games.cli import welcome_user
from brain_games.module import greet


def main():
    greet()
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        read = input('Your answer:')
        if read == correct_answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{read}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()