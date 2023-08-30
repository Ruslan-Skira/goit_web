from threading import Event, Thread
from time import sleep
import logging


def worker(event: Event):
    while True:
        sleep(1)
        logging.debug(f'Run iteration')

        if event.is_set():  # Stop Thread by checking is_set()
            break


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    e = Event()

    th = Thread(target=worker, args=(e, ))
    th.start()

    sleep(5) # Changing this will add new line of logging text.
    e.set()  # here we put set to True and is_set() -> False

    logging.debug('End program')
