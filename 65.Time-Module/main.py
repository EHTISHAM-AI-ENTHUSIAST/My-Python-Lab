import time

# Measuring how long a loop takes
start = time.time()

for i in range(5000):
    print(i)

end = time.time()
print(f"Total time taken: {end - start} seconds")

