from random import randint
from threading import Thread, RLock, Lock
import logging
from time import sleep

counter = 0
lock = RLock()
# lock = Lock()


def worker():
    global counter
    while True:
        # lock.acquire()  # For Lock
        with lock:
            #  Code that needs to be accessed by only one thread at a time
            # This thread can reacquire the lock if needed
            counter += 1
            sleep(randint(1, 3))
            with open('module03/lesson01/04_thread_lock_rlock.txt', 'a') as fd:
                fd.write(f'{counter}\n')
        # lock.release()  # For Lock


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    logging.debug('Start program')
    for i in range(5):
        th = Thread(name=f"Th#{i}", target=worker)
        th.start()

    logging.debug('End program')
