from threading import *
from time import *
from queue import *
# def display():
#   for i in range(65, 91):
#     print(chr(i))

# t = Thread(target=display)  #This makes the thread on display function
# t.start() #this will execute the thread


# for i in range(65, 91):
#   print(i)
# t.join()


# #muthx (to make thread so only one thread should be working at a time)
# def Display(str1):
#   l.acquire() #once a thread is enter it locks the function so no other threads can get inside
#   for x in str1:
#     print(x)
#     sleep(1) #sleep is used to delay printing it takes time in seconds
#   l.release() #it releases the lock

# t1 = Thread(target=Display, args=("Hello world",))
# t2 = Thread(target=Display, args=("My name is zain",))


# l = Lock() #got imported through threading
# t1.start()
# t2.start()

# t1.join()
# t2.join()


# #Semaphore (to make thread and define how many thread should work simultaneously )
# def Display(str1):
#   l.acquire() #once a thread is enter it locks the function so no other threads can get inside
#   for x in str1:
#     print(x)
#     sleep(1) #sleep is used to delay printing it takes time in seconds
#   l.release() #it releases the lock

# t1 = Thread(target=Display, args=("Hello world",))
# t2 = Thread(target=Display, args=("My name is zain",))


# l = Semaphore(1)#got imported through threading unlike lock you can give how many threads it should take at once
# t1.start()
# t2.start()

# t1.join() #join will make main thread wait for the current program to complete and then another program should be assign to main thread
# t2.join()




# #1. This is a normal method to write this code using lock and flag
# class Mydata:
#   def __init__(self):
#     self.data = 0
#     self.flag = False
#     self.lock = Lock()

#   def put(self, d):
#     while self.flag != False:
#       pass
#     self.lock.acquire()
#     self.data = d
#     self.flag = True
#     self.lock.release()

#   def get(self):
#     while self.flag != True:
#       pass
#     self.lock.acquire()
#     x = self.data
#     self.flag = False
#     self.lock.release()
#     return x


# def producer(data):
#   i = 1
#   while True:
#     data.put(i)
#     print ('Producer:', i)
#     i += 1

# def consumer(data):
#   while True:
#     x = data.get()
#     print ('Consumer:', x)

# data = Mydata()

# t1 = Thread(target= lambda:producer(data))
# t2 = Thread(target= lambda:consumer(data))

# t1.start()
# t2.start()


# t1.join()
# t2.join()


# #2. in this case we are going to use condition
# class Mydata:
#   def __init__(self):
#     self.data = 0
#     self.cv = Condition()

#   def put(self, d):
#     self.cv.acquire()
#     self.cv.wait(timeout=0)
#     self.data = d
#     self.cv.notify()
#     self.cv.release()

#   def get(self):
#     self.cv.acquire()
#     self.cv.wait(timeout=0)
#     x = self.data
#     self.cv.notify()
#     self.cv.release()
#     return x


# def producer(data):
#   i = 1
#   while True:
#     data.put(i)
#     print ('Producer:', i)
#     sleep(1)
#     i += 1

# def consumer(data):
#   while True:
#     x = data.get()
#     print ('Consumer:', x)
#     sleep(1)

# data = Mydata()
# t1 = Thread(target= lambda:producer(data))
# t2 = Thread(target= lambda:consumer(data))

# t1.start()
# t2.start()


# t1.join()
# t2.join()


#3. IN THIS CASE WE ARE GOING TO USE QUEUE TO WRITE THE SAME CODE

q = Queue()



def producer(que):
  i = 1
  while True:
    que.put(i)
    print ('Producer:', i)
    sleep(1)
    i += 1

def consumer(que):
  while True:
    x = que.get()
    print ('Consumer:', x)
    sleep(1)

t1 = Thread(target= lambda:producer(q))
t2 = Thread(target= lambda:consumer(q))

t1.start()
t2.start()


t1.join()
t2.join()
