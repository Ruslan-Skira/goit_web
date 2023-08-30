from random import randint
from threading import Timer
import logging
from time import sleep


def ruslan_check_pr(param):
    logging.debug(param)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    one = Timer(0.5, ruslan_check_pr, args=('check PR first time', ))
    one.name = 'First thread'
    one.start()

    two = Timer(1.5, ruslan_check_pr, args=('check PR I will not repeat! again', ))
    two.name = 'Second thread'
    two.start()

    sleep(2)

    two.cancel()  # the timer thread(two) cannot be reused.

    logging.debug('End program')

