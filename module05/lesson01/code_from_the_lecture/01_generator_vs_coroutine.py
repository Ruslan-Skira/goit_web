# def my_gen():
#     yield 1
#     yield 2
#     yield 3

# g = my_gen()
# print(next(g))




# def fib():
#     """Fibonachy sequence function"""
#     first = 0
#     second = 1

#     while True:
#         yield first
#         first, second = second, first+second
#         # infinity loop




# def read_file(filename, n):
#     """Function read line by line from the file."""
#     file = open(filename)

#     while True:
#         output = ''.join(file.readline() for i in range(n))
#         if output:
#             yield output
#         else:
#             break

# # Example generator with send()

def multiply_by_five():
    x = None
    while True:
        x = yield x
        x *= 5

# g = multiply_by_five()
# next(g)
# g.send(4)
# g.send('You all awesome python devs')


# # Example The same as above wit Walrus operator

# def multiply_by_five():
#     x = None
#     while x:=(yield x):
#         x *= 5

# def multiply_by_five():
#     x = None
#     while True:
#         x = yield x
#         x *= 5


# g = multiply_by_five()
# next(g)
# print(g.send(4)) # send() -> next()
# print(g.send('You all awesome python devs'))

# # Example of creating coroutines 1

# import hashlib
# def enigma():
#     output = None
#     while s:= (yield output):
#         m_hash = hashlib.md5()
#         m_hash.update(s.encode())
#         output = m_hash.hexdigest()


# secret_key_coroutine = enigma()


# secret_key_coroutine.send(None)

# print(secret_key_coroutine.send('Hello'))

# secret_key_coroutine.send(None)  # stop the service

# # Example of creating coroutines 2 wheater
# import requests

# def get_forecasts(city):
#     """Generator"""
#     wheather = requests.get(f'https://worldweather.wmo.int/en/json/{city}_en.json').json()
#     for one_forecast in wheather['city']['forecast']['forecastDay']:
#         yield one_forecast

# wheather_city = get_forecasts(2935)
# print(next(wheather_city))

# import requests

# def get_forecasts_coroutine():
#     """Coroutine"""
#     while city_id := (yield 'Send a city number or None'):
#         wheather = requests.get(f'https://worldweather.wmo.int/en/json/{city_id}_en.json').json()
#         for one_forecast in wheather['city']['forecast']['forecastDay']:
#             yield one_forecast


# wheather_city_coroutine = get_forecasts_coroutine()
# print(wheather_city_coroutine.send(123))
# # print(next(wheather_city))




# Example throw "end"
import requests

class CancelThisSh(Exception):
    pass
def get_forecasts_coroutine():
    """Coroutine"""
    while city_id := (yield 'Send a city number or None'):
        wheather = requests.get(f'https://worldweather.wmo.int/en/json/{city_id}_en.json').json()
        try:
            for one_forecast in wheather['city']['forecast']['forecastDay']:
                yield one_forecast
        except CancelThisSh:
            continue


# wheather_city_coroutine = get_forecasts_coroutine()
# wheather_city_coroutine.send(None)
# wheather_city_coroutine.send(124)
wheather_city_coroutine.throw(CancelThisSh) # raise




# print(next(wheather_city))


# #Example all in one huge generator NOT WORKING


# def combined_generator():
#     while s := (yield 'Send 1 Wheather, 2 for MD5, or None to exit'):
#         if s == 1:
#             get_forecasts_coroutine()
#         elif s == 2:
#             md5_gen()
#         else:
#             output = 'Unknow choice; try again'



# Example yield from
def combined_generator_yield_for():
    while s := (yield 'Send 1 Wheather, 2 for MD5, or None to exit'):
        if s == 1:
            yield from get_forecasts_coroutine()
        elif s == 2:
            yield from md5_gen()
        else:
            output = 'Unknow choice; try again'



