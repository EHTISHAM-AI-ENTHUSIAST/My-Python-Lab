import time

def heavy_task(name):
    print(f"Starting {name}")
    time.sleep(2)
    print(f"Finished {name}")

heavy_task("Task 1")
heavy_task("Task 2")
