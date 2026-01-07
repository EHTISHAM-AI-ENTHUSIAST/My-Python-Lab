# Python - else in Loop

for i in range(5):
    print(i)
else:
    print("Loop completed successfully without break.")

# Demonstrating else clause with break
for i in range(5):
    if i == 3:
        print("Breaking the loop at i =", i)
        break
    print(i)
else:
    print("This will not be printed because the loop was broken.")

