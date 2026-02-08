import threading
import time


def order_chai():
    for i in range(10):
        print("Ordering chai...")
        time.sleep(1)


def brew_chai():
    for i in range(10):
        print("Brewing chai...")
        time.sleep(5)


# create threads
t1 = threading.Thread(target=order_chai)
t2 = threading.Thread(target=brew_chai)

# start threads
t1.start()
t2.start()

# join threads
t1.join()
t2.join()
