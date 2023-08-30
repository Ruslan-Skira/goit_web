import threading
import time
start = time.perf_counter()
# done = False

# def worker(text):
#     counter = 0
#     while not done:
#         time.sleep(1)
#         counter += 1
#         print(f"{text}: {counter}")

# threading.Thread(target=worker, args=('OPS',)).start()
# threading.Thread(target=worker, args=('YEP',)).start()
##### Example 2
# def request_news():
#     print('Started request')
#     time.sleep(1)  # Server response
#     print('Get news')

# # request_news()
# t1= threading.Thread(target=request_news)
# t2= threading.Thread(target=request_news)

# t1.start()
# t2.start()

# t1.join()
# t2.join()
# finish = time.perf_counter()
# print(f"finished in {round(finish - start, 2)} seconds (s)")

##### Example 3 run a lot of requests news
# news_list = ['Суспільне', 'Громадське', 'Ліга', 'Українська правда', 'Укрінформ', 'Дзеркало тижня']
# def request_news(n):
#     print(f'Started request from {n}')
#     time.sleep(1)  # Server response
#     print('Get news')

# # request_news()
# threads = list()
# for i in range(len(news_list)):
#     t = threading.Thread(target=request_news, args=(news_list[i],))
#     t.start()
#     threads.append(t)

# for th in threads:
#     th.join()



# finish = time.perf_counter()
# print(f"finished in {round(finish - start, 2)} seconds (s)")

###Example 4 Thread pull executor 3.2
# import concurrent.futures
# news_list = ['Суспільне', 'Громадське', 'Ліга', 'Українська правда', 'Укрінформ', 'Дзеркало тижня']
# def request_news(n):
#     print(f'Started request from {n}')
#     time.sleep(1)  # Server request->response
#     print('line after making request')
#     return f'I got news from {n}'

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     result = [executor.submit(request_news, news_list[n]) for n in range(len(news_list))]
#     for t in concurrent.futures.as_completed(result):
#         print(t.result())


# finish = time.perf_counter()
# print(f"finished in {round(finish - start, 2)} seconds (s)")

###Example 5 Thread pull executor map method
import concurrent.futures
news_list = ['Суспільне', 'Громадське', 'Ліга', 'Українська правда', 'Укрінформ', 'Дзеркало тижня']
def request_news(n):
    print(f'Started request from {n}')
    time.sleep(1)  # Server request->response
    print('line after making request')
    return f'I got news from {n}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(request_news, news_list)  # It will allow wait when all done.
    for r in results:
        print(r)


finish = time.perf_counter()

print(f"finished in {round(finish - start, 2)} seconds (s)")


