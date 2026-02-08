from multiprocessing import Process, Value


def increment(counter):
    for _ in range(1000):
        with counter.get_lock():
            counter.value += 1


if __name__ == "__main__":
    counter = Value("i", 0)
    processes = [
        Process(target=increment, args=(counter,)) for _ in range(10)
    ]  # store the threads in the array for join and start later on
    [p.start() for p in processes]
    [p.join() for p in processes]
    print(f"Counter value is {counter.value}")  # 10000
