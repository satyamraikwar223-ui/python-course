import threading 
import time 
from concurrent.futures import ThreadPoolExecutor

# indicate some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

def main():
    time1 = time.perf_counter()

    # normal code
    # func(1)
    # func(2)
    # func(3)

    # same code using threads
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[4])
    t3 = threading.Thread(target=func, args=[4])

    t1.start()
    t2.start()
    t3.start()
    # output
    # Sleeping for 4 seconds
    # Sleeping for 4 seconds
    # Sleeping for 4 seconds
    # 0.01918960001785308

    t1.join()
    t2.join()
    t3.join()
    # output
    # Sleeping for 4 seconds
    # Sleeping for 4 seconds
    # Sleeping for 4 seconds
    # 4.088913600018714

    # counting time
    time2 = time.perf_counter()
    print(time2-time1)



def poolingDemo():
    with ThreadPoolExecutor(max_workers=1) as executor:
     #future = executor.submit(func, 3)
     #future = executor.submit(func, 2)    
     #future = executor.submit(func, 5)
     #print(future.result())
     #print(future.result())
     #print(future.result())

#map executor
     l = [3, 5, 4, 2]
     results = executor.map(func, l)
     for result in results:
         print(result)
    
poolingDemo()

