import time
import functools
from functools import lru_cache


@lru_cache(maxsize=None)  # maxsize=None means unlimited cache
def fx(n):
    time.sleep(2)  # suppose this is a time-consuming calculation
    return n * 5


# --- first calls ---
print(fx(20))  # this will take 2 seconds
print(fx(10))  # this will take 2 seconds
print(fx(5))  # this will take 2 seconds
print("first calls completed!\n")

# --- second calls ---
print(fx(20))  # this will be instant
print(fx(10))  # this will be instant
print(fx(5))  # this will be instant
print("second calls completed!")
