from rudp.thread import Thread
import queue

class Actor(Thread):
    def __init__(self, maxsize = 0):
        super().__init__()
        self.queue = queue.Queue(maxsize)

    def put(self, data):
        self.queue.put(data)

    def get(self):
        return self.queue.get()

    def task_done(self):
        self.queue.task_done()

    def stop(self):
        self.queue.put(None)
        self.queue.join()
        self.join()
