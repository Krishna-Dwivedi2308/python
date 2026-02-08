import threading
import time
import os


def brew_chai():
    print(f"Process ID: {os.getpid()}")
    print(f"{threading.current_thread().name} statrted brewing")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing")


thread1 = threading.Thread(target=brew_chai, name="Barista-1")
thread2 = threading.Thread(target=brew_chai, name="Barista-2")

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()

print(f"total time taken : {end-start:.2f} seconds")
