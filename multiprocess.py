# importing the multiprocessing module
import multiprocessing
import pyaudio
import wave
import time
import struct
import numpy as np
#import matplotlib.pyplot as plt
#from tkinter import TclError


def print_cube(num, vector, lock):
   for x in range(num):
      lock.acquire()
      vector[x] = x*x*x
      lock.release()
      print("Cube: {}".format(x * x * x))
      time.sleep(2)


def print_square(num, vector, lock):
   print("Square: {}".format(num * num))
   #for x in vector:
      #print(vector)

# Define function to play the sound on a thread
def play_sound( threadName, delay, chunk_shared, lock):
   wf = wave.open ("test.wav", 'rb')
   p = pyaudio.PyAudio()
   chunk = 1024

   stream = p.open(
      format=p.get_format_from_width(wf.getsampwidth()),
      channels=wf.getnchannels(),
      rate=wf.getframerate(),
      output=True
      )
   data = wf.readframes(chunk)
   print(data[:])
   buffer = [x for x in data] #convert byte list to int list
   print(buffer)
   i = 0
   for elem in buffer:
      #print(elem)
      chunk_shared[i] = elem
      ++i
   print(chunk_shared)
   #print([type(x) for x in buffer])
   #print("Quantidade de elementos:")
   #print(len(chunk_shared));


   while data != '':
      stream.write(data)
      data = wf.readframes(chunk)
      #print(data)
   stream.close()
   p.terminate

# Define a test function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 15:
      time.sleep(delay)
      count += 1
      string = threadName + ':' + time.ctime(time.time())
      print(string)
      #print"%s: %s" % ( threadName, time.ctime(time.time()) )

#TODO: Define function to do the FFT
#TODO: Define function to plot point cloud model

if __name__ == "__main__":
    lock = multiprocessing.Lock()
    #creating shared memory
    vector = multiprocessing.Array('i', 10)
    chunk_shared = multiprocessing.Array('i', 4096);

    # creating processes
    p1 = multiprocessing.Process(target=print_cube, args=(10, vector, lock))
    p2 = multiprocessing.Process(target=print_square, args=(10, vector, lock))
    p3 = multiprocessing.Process(target=print_time, args=("Thread-3",2))
    p4 = multiprocessing.Process(target=play_sound, args=("Thread-4",2, chunk_shared, lock))

    # starting process
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    # wait until the process is finished
    p1.join()
    p2.join()
    p3.join()

    print(vector[:])
    #print(chunk_shared)
    #print("Quantidade de elementos:")
    #print(len(chunk_shared));

    p4.join()

    # all the processes finished
    print("Done!")
