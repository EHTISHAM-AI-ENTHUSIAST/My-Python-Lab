from multiprocessing import Process
import time

def heavy_task(name):
    print(f"Starting {name}")
    time.sleep(2)
    print(f"Finished {name}")

if __name__ == "__main__":
    p1 = Process(target=heavy_task, args=("Task 1",))
    p2 = Process(target=heavy_task, args=("Task 2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("All processes finished")
