import threading

chai_stock = 0


def restock():
    global chai_stock
    for _ in range(10_000_000):
        chai_stock += 1


threads = [threading.Thread(target=restock) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(chai_stock)
