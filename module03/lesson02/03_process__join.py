import sys
from multiprocessing import Process
from time import sleep
import os

# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())

def example_work(params):
    sleep(0.5)
    print(params)
    # info('function example_work') # Process ID
    sys.exit(0)


if __name__ == '__main__':
    prs = []
    for i in range(5):
        pr = Process(target=example_work, args=(f"Count process - {i}",))  # daemon=True
        pr.start()
        prs.append(pr)

    [el.join() for el in prs]

    print('End program')
