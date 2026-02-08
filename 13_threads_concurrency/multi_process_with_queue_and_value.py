import threading
import time
from multiprocessing import Process

# def cpu_heavy():
#     print(f"Crunching some numbers")
#     total=0
#     for i in range(10**7):
#         total+=i
#     print(f"Done crunching {total}")

# start=time.time()
# threads=[threading.Thread(target=cpu_heavy) for _ in range(10)] #store the threads in the array for join and start later on
# [t.start() for t in threads]
# [t.join() for t in threads]

# print(f"Time Taken : {time.time()-start:.2f} seconds")

# Time Taken : #4.58

# -------------------------------------------
import threading
import time


def cpu_heavy():
    print(f"Crunching some numbers")
    total = 0
    for i in range(10**9):
        total += i
    print(f"Done crunching {total}")


if __name__ == "__main__":
    start = time.time()
    threads = [
        Process(target=cpu_heavy) for _ in range(10)
    ]  # store the threads in the array for join and start later on
    [t.start() for t in threads]
    [t.join() for t in threads]

    print(f"Time Taken : {time.time()-start:.2f} seconds")
    # Time Taken : 1.67 seconds
