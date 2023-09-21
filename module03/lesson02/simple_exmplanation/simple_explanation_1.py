import multiprocessing as mp
import time
import math

start =  time.perf_counter()

r1 = []
r2 = []
r3 = []

def make_calc_one(numbers: list):
    for number in numbers:
        r1.append(math.sqrt(number ** 3))

def make_calc_two(numbers: list):
    for number in numbers:
        r2.append(math.sqrt(number ** 5))

def make_calc_three(numbers: list):
    for number in numbers:
        r3.append(math.sqrt(number ** 3))



# ### Example 1 no multiprocessing
# if __name__ == "__main__":
#    number_list = list(range(5000_000))

#    make_calc_one(number_list)
#    make_calc_two(number_list)
#    make_calc_three(number_list)

#    finish =  time.perf_counter()

#    print(finish-start)

# ### Example 2 multiprocessing
if __name__ == "__main__":
   number_list = list(range(5000_000))
   p1 = mp.Process(target=make_calc_one, args=(number_list,))
   p2 = mp.Process(target=make_calc_two, args=(number_list,))
   p3 = mp.Process(target=make_calc_three, args=(number_list,))

   p1.start()
   p2.start()
   p3.start()

   finish =  time.perf_counter()
   print(finish-start)


