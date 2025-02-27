import random
from brain_games.engine import check_answer


def progression_games(name):
    print('What number is missing in the progression?')
    progression = []
    count = 0
    while count < 3:
        long_progression = random.randint(5, 10)
        point_progression = random.randint(1, long_progression)
        start_progression = random.randint(1, 50)
        step_progression = random.randint(1, 5)
        for i in range(1, long_progression + 1):
            if i != point_progression:
                progression.append(str(start_progression + (step_progression * i)))
            else:
                progression.append('..')
                correct_answer = start_progression + (step_progression * i)
        print(f'Question: {" ".join(progression)}')
        if check_answer(str(correct_answer), name):
            count += 1
            progression = []
        else:
            break
    if count == 3:
        print(f'Congratulations, {name}!')
