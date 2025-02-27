import random
from brain_games.engine import check_answer


def gcd_games(name):
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f'Question: {num1} {num2}')
        for i in range(1, min(num1, num2) + 1):
            if num1 % i == 0 and num2 % i == 0:
                correct_answer = i
        if check_answer(str(correct_answer), name):
            count += 1
        else:
            break
    if count == 3:
        print(f'Congratulations, {name}!')