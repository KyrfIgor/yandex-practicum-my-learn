from multiprocessing import Process
from multiprocessing.queues import Queue
import multiprocessing as mp


#################################################################################
class Worker(Process):
    def __init__(self, func, func_args, queue):
        self._func = func
        self._func_args = func_args
        self._queue = queue
        super().__init__(target=self._func, args=(self._queue,))

    def run(self):
        # Вызов передаваемого метода и заполнение очереди
        self._queue.put(self._func(*self._func_args))
##################################################################################

def plus(a):
    print(a + 10)
    return a + 10


if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    my_queue = Queue(ctx=ctx)
    worker = Worker(plus, [1, 2, 3, 4], my_queue)
    worker.start()
    worker.join()
