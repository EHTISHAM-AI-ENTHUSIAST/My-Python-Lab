def sum_all(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    print("Total:", total)

sum_all(5, 10)

sum_all(1, 2, 8, 4, 5)