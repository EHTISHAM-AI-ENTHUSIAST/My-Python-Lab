marks = [77, 97, 64, 35, 55]


def failing(score):
    return score < 70


failed = filter(failing, marks)
print("Failing Scores:", list(failed))
