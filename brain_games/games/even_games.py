import random
from brain_games.engine import check_answer

def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if check_answer(correct_answer, input('Your answer: '), name):
            count += 1
        else:
            break
    if count == 3:
        print(f'Congratulations, {name}!')