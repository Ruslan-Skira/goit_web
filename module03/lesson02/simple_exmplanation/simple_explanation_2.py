import multiprocessing as mp
import time
start = time.perf_counter()

# from MIV.module import function_name




def render_photo()-> None:
    print(f'Started rendering')
    time.sleep(3)  # Server response
    print('Rendering ended')

### Example 1
# render_photo()
# render_photo()
# render_photo()

### Example 2 Creating Processes
if __name__ == "__main__":  # Need to start processes here, under the __name__
    # p1 = mp.Process(target=render_photo)
    # p2 = mp.Process(target=render_photo)
    # p3 = mp.Process(target=render_photo)

    # p1.start()
    # p2.start()
    # p3.start()

    # p1.join()
    # p2.join()
    # p3.join()

    processes = []

    for _ in range(10):
        p = mp.Process(target=render_photo)
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()
    print(f"Finished in {round(finish -start, 2)} second(s)")


