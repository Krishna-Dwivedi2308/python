from multiprocessing import Process
from multiprocessing import Queue


def prepare_chai(queue):
    queue.put("chai")


if (
    __name__ == "__main__"
):  # this ensures that only the main process runs this part of the code and not the child process. otherwise during the creation of new processes during multiprocessing, entire scripts would get reimported and run . So , this guardrail is crucial .
    # prepare_chai(queue)
    queue = Queue()
    p = Process(target=prepare_chai, args=(queue,))
    p.start()
    p.join()
    print(queue.get())
