import threading
import time


def boil_milk():
    print("Boiling milk...")
    time.sleep(5)
    print("Milk boiled.🎉")


def toast_bun():
    print("Toasting bun...")
    time.sleep(3)
    print("Bun toasted.🎉")


start = time.time()
boil_milk()
toast_bun()
end = time.time()
print(f"total time taken : {end-start:.2f} seconds")
print("-----------------------")
start = time.time()
thread1 = threading.Thread(target=boil_milk)
thread2 = threading.Thread(target=toast_bun)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
end = time.time()
print(f"total time taken : {end-start:.2f} seconds")
