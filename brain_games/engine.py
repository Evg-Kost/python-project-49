def check_answer(correct_answer, name):
    answer = input('Your answer:')
    if correct_answer == answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        return False