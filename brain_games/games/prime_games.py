import random

from brain_games.engine import check_answer


def prime_games(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        if number == 1:
            correct_answer = 'no'
        elif number == 2:
            correct_answer = 'yes'
        else:
            for i in range(2, number):
                if number % i == 0:
                    correct_answer = 'no'
                    break
                else:
                    correct_answer = 'yes'
        if check_answer(correct_answer, name):
            count += 1
        else:
            break
    if count == 3:
        print(f'Congratulations, {name}!')
