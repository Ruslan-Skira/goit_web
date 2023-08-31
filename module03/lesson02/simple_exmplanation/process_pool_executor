import time
import concurrent.futures
"""
1.automatically join results
"""
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
# Use it with 'context manager'
start = time.perf_counter()



def render_photo()-> None:
    print(f'Started rendering')
    time.sleep(3)  # Server response
    return 'Rendering ended'

if __name__ == '__main__':
    # # Example 1 one process
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     f1 = executor.submit(render_photo)
    #     print(f1.result()) # what function return

    # # Example 2 any ammount of  process
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     result = [executor.submit(render_photo) for _ in range(10)]

    #     for f in concurrent.futures.as_completed(result):
    #         print(f.result()) # what function return

    # Example 3 any ammount of  process
    with concurrent.futures.ProcessPoolExecutor() as executor:
        result = [executor.submit(render_photo) for _ in range(10)]

        for f in concurrent.futures.as_completed(result):
            info('main line')
            print(f.result()) # what function return

    finish = time.perf_counter()
    print(f"Finished in {round(finish -start, 2)} second(s)")
