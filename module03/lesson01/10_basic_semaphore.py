from threading import Semaphore, Thread
from time import sleep
import logging


def worker(semaphore: Semaphore):
    logging.debug(f'Wait...')
    with semaphore:
        # Access the shared resource
        # When the semaphore count reaches 0, other threads will block
        logging.debug(f'Got semaphore')
        sleep(1)
    logging.debug(f'finished')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    pool = Semaphore(2)  # Allows 2 concurrent threads
    w1 = Thread(target=worker, args=(pool, ))
    w2 = Thread(target=worker, args=(pool, ))
    w3 = Thread(target=worker, args=(pool, ))

    w1.start()
    w2.start()
    w3.start()
