import threading
import time


def task1():
    for i in range(3):
        print("Task 1 running")
        time.sleep(2)


def task2():
    for i in range(3):
        print("Task 2 running")
        time.sleep(2)


t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()

print("All tasks finished")


'''
.start() vs .join()

t.start()
This means: “Start your work now, and I will continue to the next line without waiting.”

t.join()
This means: “Wait! Do not move forward until thread `t` has finished its work.”
(It is used when we need to wait for all results to be completed.)

'''