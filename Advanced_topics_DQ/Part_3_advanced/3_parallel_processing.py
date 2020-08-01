# 8/1/2020 Saidakbar P. Object-Oriented Programming: computer memory, parallel processing
my_int = 42
int_addr = id(my_int) # returns memory address for my_int
my_str = 'hello'
str_addr = id(my_str)
##
import sys

my_int = 200
size_of_my_int = sys.getsizeof(my_int) # shows size in bytes

int1 = 10
int2 = 100000
str1 = "Hello"
str2 = "Hi"
int_diff = sys.getsizeof(int1) - sys.getsizeof(int2) # 0
str_diff = sys.getsizeof(str1) - sys.getsizeof(str2) # 3

# accessing data from RAM is much faster than disk storage
import time
import csv

start_file_time = time.clock()
f = open("list.csv", "r")
list_from_file = list(csv.reader(f))
end_file_time = time.clock()

file_time = end_file_time - start_file_time
print(file_time) # 0.000777
before = time.clock()
list_from_RAM = "1,2,3,4,5,6,7,8,9,10".split(",")
after = time.clock()
RAM_time = after - before
print(RAM_time) # 0.000148
# Computer has a program counter that indicates the current instruction to execute in CPU
# parallel computing
# we can perform parallel computing on mutable data types on a multi core CPU
class Counter():
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get_count(self):
        return self.count

def count_up_100000(counter):
    for i in range(100000):
        counter.increment()

import threading # library for creating multiple threads

counter = Counter()
# create another thread to run concurrently with counter instance: count_up_100000 function
thread = threading.Thread(target=count_up_100000, args=[counter])
# start the thread
thread.start()
# join the thread to main thread. Main thread waits for count_thread to finish. This is called blocking.
thread.join()
after_join = counter.get_count()

# multithreaded code is nondeterminic when it starts.
def conduct_trial():
    counter = Counter()
    count_thread = threading.Thread(target=count_up_100000, args=[counter])
    count_thread.start()
    # Take measurement 
    c=counter.get_count() # nondeterministic value in the thread
    count_thread.join()
    return c
trial1 = conduct_trial() # different values each time
trial2 = conduct_trial()
trial3 = conduct_trial()

# we can use a locking mechanism to allow one thread to perform action while the other thread waits for the lock to end
import threading

class Counter():
    def __init__(self):
        self.lock = threading.Lock() # instantiating Lock for atomicity of the increment function. Otherwise, we will not get our correct 200k count
        self.count = 0
    def increment(self):
        self.lock.acquire() # acquire lock for one thread so the other thread does not interfere with this functions atomicity
        old_count = self.count
        self.count = old_count + 1
        self.lock.release() # release lock for the other thread to use
    def get_count(self):
        return self.count

def count_up_100000(counter):
    for i in range(100000): # count up to 100k
        counter.increment()

def conduct_trial():
    counter = Counter()
    # create two threads to count up to 200k
    count_thread1 = threading.Thread(target=count_up_100000, args=[counter])
    count_thread2 = threading.Thread(target=count_up_100000, args=[counter])
    # 2 threads are starting
    count_thread1.start()
    count_thread2.start()
    # two threads are joining the main thread
    count_thread1.join()
    count_thread2.join()
    # we will get consistent results here: 200k
    final_count = counter.get_count()
    return final_count

trial1 = conduct_trial() # 200k
trial2 = conduct_trial() # 200k
trial3 = conduct_trial() # 200k