from multiprocessing import Process
import sys


def example_work(params):
    print(params)
    sys.exit(123)  # exit the interpreter


if __name__ == '__main__':
    process = []
    for i in range(5):
        pr = Process(target=example_work, args=(f"Count process - {i}",))
        pr.start()
        process.append(pr)

    [print(pr.exitcode, end=" ") for pr in process]  # exitcode None process not ended

    print('\n', '*'*8, sep='\n')

    [pr.join() for pr in process]
    print('After join')

    [print(pr.exitcode, end=" ") for pr in process]  # 0 process ended or N from sys.exit(N)
