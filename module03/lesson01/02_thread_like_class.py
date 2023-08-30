from random import randint
from threading import Thread
import logging
from time import sleep

"""Every Python program has at least one thread of execution called the main thread. Both processes and threads are created and managed by the underlying operating system.
Return the main Thread object. In normal conditions, the main thread is the thread from which the Python interpreter was started."""
class MyThread(Thread):

    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args

    def run(self):
        sleep(randint(1, 3))
        logging.debug(f"In my thread: {self.args}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    threads = []
    for i in range(5):
        th = MyThread(name=f"Th#{i}", args=(f"Count thread - {i}", ))  # daemon=True
        th.start() # Call the run command
        threads.append(th)

    [th.join() for th in threads]
    sleep(2)
    logging.debug('End program')
