import multiprocessing
import time

def heavy_calc(number):
    print(f"Starting calculation for {number}...")
    # Pretend this is a heavy math task taking 2 seconds
    time.sleep(2)
    result = number * number
    print(f"Finished! Square is {result}")

if __name__ == "__main__":
    # This block is required so that the new process does not get confused

    # Creating 2 separate processes 
    p1 = multiprocessing.Process(target=heavy_calc, args=(10,))
    p2 = multiprocessing.Process(target=heavy_calc, args=(20,))

    # Starting them (They will run in parallel)
    p1.start()
    p2.start()

    # Wait for them to finish
    p1.join()
    p2.join()

    print("All processes done!")
