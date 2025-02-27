import random
from brain_games.engine import check_answer


def calc_games(name):
    print('What is the result of the expression?')
    count = 0
    while count < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        expression = random.choice(['+', '-', '*'])
        print(f'{num1} {expression} {num2}')
        if expression == '+':
            correct_answer = num1 + num2
        elif expression == '-':
            correct_answer = num1 - num2
        else:
            correct_answer = num1 * num2
        if check_answer(str(correct_answer), input('Your answer: '), name):
            count += 1
        else:
            break
    if count == 3:
        print(f'Congratulations, {name}!')