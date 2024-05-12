'''
Multi threading:

Multi tasking:executing several tasks simultaneously is called multi tasking.

2 types of multi tasking
1)process based multi tasking
2)thread based multi tasking

1)process based multi tasking:(best suited at os level)
Executing several tasks simultaneously where each task is separate independent  process.

Ex:
Typing some code on computer ====>typing process
Downloading some file from internet ===> downloading process
Listening to music ===> music process

above 3 process are nowhere related to each other

2)thread based multi tasking:(best suited at programming level)
executing several task simultaneously where each task is separate independent part of same process.
Each independent part is called as thread.

Ex: GMAIL where many users can send mails to same person simultaneously.Each mail is separate thread

NOTE: whenever there is a dependancy we shouldnt choose multithreading concept

Thread:
1)Flow of execution
2)for every thread there is some job available
3)by default every program will have one thread(main)

inbuilt module threading is used to import thread concept
and a method current_thread().getName() gives current executing thread

there are 3 ways of creating thread in python
1)Creating a thread without using any class
2)Creating a thread by extending a thread class  (best approach)
3)Creating a thread without extending a thread class

'''
'''
#Creating a thread without using any class

from threading import *

def display():
    print('display method is executed by ',current_thread().getName())

t=Thread(target=display)   # main thread creates child thread
t.start()                  # child thread starts executing targeted thread
print('this is executed by ',current_thread().getName())

# in multithreading output order isnt confirmed

def show():
    for i in range(10):
        print('In child thread')

t=Thread(target=show).start()   # we can start thread in same line of its creation
for j in range(10):
    print('In main thread')

# Creating a thread by extending a thread class

class MyThread(Thread):

    def run(self):                # run() is overriden by child class
        for i in range(5):      # whatever presents inside run method is the task of child class to execute
            print('In child thread 1')

t=MyThread()    # no need to pass target statements under run will be executed by child thread
t.start()
for i in range(5):
    print('in main thread 1')

# Creating a thread without extending a thread class

from threading import *
from time import sleep

class VlcPlayer:

    def audio(self):   # instance method
        for i in range(3):
            print('audio is playing')
            sleep(2)

    def video(self):
        for i in range(3):
            print('video is playing')
            sleep(2)

v=VlcPlayer()     # object is created to call instance methods
t1=Thread(target=v.audio)      # child thread is created to execute audio()
t2=Thread(target=v.video)    # if we dont Extend thread method we have to target the task to child thread
t1.start()
sleep(2)     # to avoid collision
t2.start()
t1.join()
t2.join()
print('done')


To give some time b/w execution we can use sleep() concept

from time import sleep
after print statement use sleep(2)   # 2 is seconds here

join() is used to ask main thread to execute once child thread done

t1.join()

from threading import *
from time import *
def even(n):
    for i in n:
        if i%2!=0:
            n.remove(i)
    print(n)
    sleep(2)

def odd(n):
    for i in n:
        if i%2==0:
            n.remove(i)
    print(n)
    sleep(2)

lst=[1,2,3,4,5,6,7,8,9]
lsst=[1,2,3,4,5,6,7,8,9]

begintime=time()
t1=Thread(target=even(lst))
t2=Thread(target=odd(lsst))
t1.start()
sleep(2)
t2.start()
endtime=time()
print('total time taken is ',endtime-begintime)

'''
'''

from threading import *
from time import *

class MyThread(Thread):
    def run(self) :
        for i in range(5):
            print('In run method',i)
            sleep(5)
print(current_thread().getName())

t=MyThread()
t.start()
for i in range(5):
    print('In main thread', i)
    sleep(5)
t.join()
print(current_thread().getName())
'''
'''
to set name for thread we use setname() method

to get unique identity number for every thread we use ident

to get number of active threads we can use active_count
'''
'''
from threading import *
def show():
    print('child thread')
    print(current_thread().setName('sri'))

print('number of active threads',active_count())
t=Thread(target=show,name='child 1')    # we can set name for child thread while creating
t.start()
print(current_thread().getName())
print('main thread identification number is',current_thread().ident)
print('child thread identification is',t.ident)
print(t.getName())
print('number of active threads',active_count())

'''
'''
enumerate:

to get count and info  of all active threads

to check if the thread is alive we use isAlive()

'''
'''
from threading import *
from time import *

def info():
    print('in child thread')
    sleep(2)
print('number of active threads',active_count())

t1=Thread(target=info,name='child 1')
t2=Thread(target=info,name='child 2')
t3=Thread(target=info,name='child 3')
t4=Thread(target=info,name='child 4')
t1.start()
t2.start()
t3.start()
t4.start()
print('number of active threads',active_count())
print(t1.name,'is alive',t1.is_alive())
print(t2.name,'is alive',t2.is_alive())


e=enumerate()

for i in e:
    print('thread name',i.name)
    print('thread identification number',i.ident)
    print()

sleep(5)
print(t1.name,'is alive',t1.is_alive())
print(t2.name,'is alive',t2.is_alive())

'''
'''
from threading import *
from time import *

class MyThread:

    def __init__(self,lan):
        self.lan=lan

    def audio(self):
        for i in range(5):
            print(self.lan,'song is playing')
            sleep(2)

    def video(self):
        for j in range(5):
            print(self.lan, 'video is playing')
            sleep(2)

print('total number of threads before child threads is ',active_count())

m=MyThread('kannada')
t1=Thread(target=m.audio(),name='child1')
t2=Thread(target=m.video(),name='child2')
begintime=time()
t1.start()
t2.start()
print('total number of threads after child threads is ',active_count())
endtime=time()
print('total time taken is ',endtime-begintime)

'''
'''
from threading import *
from time import *

class New_Thread(Thread):
    def __init__(self,n):
        self.n=n
        super().__init__()                # Thread parent class has to be invoked

    def run(self):
        for i in range(self.n):
            print('welcome')
            sleep(2)
print('current thread is :',current_thread().getName())
print('no of active threads are :',active_count())
begintime=time()
t1=New_Thread(5)
t1.setName('sri')
t1.start()
t1.join()
print('current thread is :',t1.getName())
print('no of active threads are :',active_count())
print('t is alive',t1.is_alive())
endtime=time()
print('total time taken is :',endtime-begintime)


Daemon threads:

Thread which do background task like garbage collection and whose purpose is to 
support for non daemon threads(like main thread)

EX:garbage collector

1)to check if the tgread is daemon we use
thread_name.isDaemon()     # method
thread_name.daemon         # variable name

2) to set the thread we use setDaemon() method
thread_name.setDaemon(True)    # to set thread as daemon if we give False thread will be non daemonic
Note: we can set the thread as daemon only when the thread isnt active(before starting)
if we try to set active thread as daemon we get RuntimeError

3) By default only main thread is non daemon
4) child threads will inherit daemon property from parent threads,
if parent thread is daemonic so is child thread and vice versa.
if we are creating first thread then main thread will be its parent thread
we can set child thread as daemon on requirement

'''
'''
def job():
    for i in range(5):
        print('In child thread')

print('Is current thread daemon ',current_thread().isDaemon())
print('Is current thread daemon ',current_thread().daemon)

t=Thread(target=job(),name='sri')
print('Is t daemon ',t.isDaemon())
t.setDaemon(True)                    # to set t thread as daemon
print('After setting t as daemon',t.daemon)

# illustation for child thread inheriting daemon propery from parent thread

from threading import *
from time import *

def task1():
    print('executed by child t1')
    t2 = Thread(target=task2, name='muki')    # t1 is parent thread for t2
    print('t2 is daemon thread ',t2.daemon)
    t2.start()

def task2():
    print('executed by child t2')

t1=Thread(target=task1,name='sri')
print('t1 is daemon thread (before)',t1.daemon)
t1.setDaemon(True)
print('t1 is daemon thread (after)',t1.daemon)
t1.start()
t1.join()
sleep(10)

'''
'''
whenever last non daemon thread terminates,automatically all daemon threads will terminated,
we need not terminate explicitly..

ex:
in car racing game

cars-----non daemon threads
background sceneries(lights,roads)------daemon threads

in car race when last car stops all background will be automatically stops 

supporting tasks can be implemented by daemon threads
main tasks can be implemented by non daemon threads
'''
'''
def isdaemon():
    for i in range(10):
        print('executed by child thread t')
        sleep(2)

t=Thread(target=isdaemon)
t.setDaemon(True)
t.start()
sleep(4)
print('end of no daemon thread(main)')    # main thread is sleeping for 4 seconds then starts once its done
# daemon thread will ends automatically.


import threading
from threading import *

lock=threading.Lock()
x=0
def increment():
    global x
    x+=1

def thread_task():
    lock.acquire()
    for i in range(10):
        increment()
    lock.release()

t1=Thread(target=thread_task)
t2=Thread(target=thread_task)
t1.start()
t2.start()
t1.join()
t2.join()
for i in range(10):
    print('x={} at {}'.format(x,i))

'''
'''
Thread synchronization is defined as a mechanism which ensures that 
two or more concurrent threads do not simultaneously execute some particular program segment 
known as critical section.

1)when 2 threads try to execute same logic or same functionality we reach deadlock situation
2)deadlock can be managed using syncronisation locks

Lock class provides following methods:

acquire([blocking]) : To acquire a lock. A lock can be blocking or non-blocking.
When invoked with the blocking argument set to True (the default), 
thread execution is blocked until the lock is unlocked, then lock is set to locked and return True.
When invoked with the blocking argument set to False, thread execution is not blocked. 
If lock is unlocked, then set it to locked and return True else return False immediately.

release() : To release a lock.
When the lock is locked, reset it to unlocked, and return.
 If any other threads are blocked waiting for the lock to become unlocked, 
 allow exactly one of them to proceed.
If lock is already unlocked, a ThreadError is raised.
'''

import threading
from threading import *
x=0       # global variable
def increment():
    global x
    for i in range(100):
        x+=1
        print(x)



t1=Thread(target=increment)
t2=Thread(target=increment)
t1.start()
t2.start()

# same program using locks

y=0       # global variable
def increment1():
    global y
    lock.acquire()
    for i in range(100):
        y+=1
        print(y)
    lock.release()


lock=threading.Lock()          # creating thread lock object
t1=Thread(target=increment1)
t2=Thread(target=increment1)
t1.start()
t1.join()
t2.start()
t2.join()


# to run same thread 10 times
from threading import *
import time
def hello():
    print('welcome')
    time.sleep(5)
    print('done')


a = time.time()
threads = []   # to store the threads
for _ in range(10):  # loop to run the thread 10 times
    t = Thread(target=hello)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
b = time.time()

'''
concurrent.features:
1)used for running asynchronous task either with threads using ThreadPoolExecutor or 
with separate process using ProcessPoolExecutor
2)both ThreadPoolExecutor and ProcessPoolExecutor are subclass of abstract class Executor

syntax to Initializes a new ThreadPoolExecutor instance
    concurrent.features.ThreadPoolExecutor(self, max_workers=None, 
    thread_name_prefix='', initializer=None, initargs=())
    
    max_worker--maximum no of threads that can be used to run,default is 5
    thread_name_prefix--optional thread name to give
    initializer---callable/function to initialize threads
    initargs---tuple of arguments to pass to initializer
    
submit(*args, **kwargs)
    submits the function/callable to be executed with given arguments and returns the 
    future object representing the execution(return vallue) of the function
    
map(self, fn, *iterables, timeout=None, chunksize=1)
    Returns an iterator equivalent to map(fn, iter).
    fn--input function to be executed
    
    iterables--iterables to be used
    
    timeout--the max no of seconds to wait ,if none given then waits unlimited seconds
    
    chunksize--used by only ProcessPoolExecutor not ThreadPoolExecutor
    

future object gives results
class concurrent.futures.Future

methods
    cancel()--attempt to cancel the function currently executing,if already finished 
    or running and cannot be cancelled returns False otherwise call will be 
    cancelled and retrurned True
    
    cancelled()--returns True if call is cancelled currently
    
    running()--returns True if call is running currently
    
    done()--returns True if the function is cancelled or completed successfully
    
future_object.results()
        returns results of function,if the function is not completed waits upto
        timeout seconds,if hasnt completed in timeout seconds then throws TimeOutError
        
        if the future is cancelled throws CancelledError
        
as_completed(fs, timeout=None)

An iterator over the given futures that yields each as it completes.
    
    fs---sequence of future objects to iterate over 
    timeout--maximum no of seconds to wait
    
returns iterator object that yields the given future as they complete (finished or completed)
if the futures are duplicated they will be returned once

throws TimeoutError if the iterator could not be generated before given timeout 
'''
import concurrent.futures
import time
def hello(seconds):
    print(f'sleeping for {seconds} secondss')
    time.sleep(seconds)
    print('done sleeping')
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    future_object=executor.submit(hello,5)   # submits the function to be executed
    future_object=executor.submit(hello,10)   # we can create as many as future objects
print(future_object.result())   # printing results


# using as-completed()

import concurrent.futures
import time

def hello(seconds):
    print(f'sleeping for {seconds} secondss')
    time.sleep(seconds)
    print('done sleeping')

a = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # # can be used loop instead of list comprehension
    future_object = [(executor.submit(hello, 5)) for _ in range(10)]
    # above list compre creates list of future objects
    as_completed_object = concurrent.futures.as_completed(future_object, timeout=5)
    # as_completed method takes different future objects and returns iterator
    for f in as_completed_object:
        print(f.result())   # printing results of future objects

b = time.perf_counter()

# using map function

with concurrent.futures.ThreadPoolExecutor(max_workers=5,
                                    thread_name_prefix='sri') as executor:
    lst=[5,4,3,2,1]
    results=executor.map(hello,lst)
    for f in results:
        print(f)
# # map returns results of function call than future object

# program for downloading images from net and writing onto new file and executing using multi threading

import requests
import  concurrent.futures

urls=['https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F143130094388363480%2F&psig=AOvVaw2718Q_iMe2OvWNy5_QaEbt&ust=1587708746656000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLi_g6S0gOkCFQAAAAAdAAAAABAD',
     'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.ecopetit.cat%2Fecvi%2FiTTRhRT_green-grass-and-blue-sky%2F&psig=AOvVaw2718Q_iMe2OvWNy5_QaEbt&ust=1587708746656000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLi_g6S0gOkCFQAAAAAdAAAAABAI',
      'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.jakpost.travel%2Fvwall%2Fhhiwix_beautiful-nature-autumn-full-hd-wallpapers-background-high%2F&psig=AOvVaw2718Q_iMe2OvWNy5_QaEbt&ust=1587708746656000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLi_g6S0gOkCFQAAAAAdAAAAABAO',
      'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwonderfulengineering.com%2F50-nature-wallpapers-hd-for-free-download%2F&psig=AOvVaw2718Q_iMe2OvWNy5_QaEbt&ust=1587708746656000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCLi_g6S0gOkCFQAAAAAdAAAAABAU']


def download(url):
#for url in urls:
    result=requests.get(url).content
    image_name=url.split('/')[3]
    image_names=f'{image_name}.jpg'
    with open('images','wb') as new_file:
        new_file.write(result)
        print(f'{image_names} downloaded')

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(download,urls)