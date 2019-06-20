# importing the multiprocessing module
import multiprocessing
import pyaudio
import wave
import time
import struct
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
#from tkinter import TclError
import pptk
import numpy as np
import plyfile


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
def play_sound( threadName, delay, chunk_shared, lock, is_playing_audio):
   wf = wave.open ("test.wav", 'rb')
   p = pyaudio.PyAudio()
   chunk = 1024 * 4

   stream = p.open(
      format=p.get_format_from_width(wf.getsampwidth()),
      channels=wf.getnchannels(),
      rate=wf.getframerate(),
      output=True
      )
   data = wf.readframes(chunk)
   #print(data[:])

   while data != '':
      is_playing_audio.Value = 1
      stream.write(data)
      data = wf.readframes(chunk)
   stream.close()
   is_playing_audio.Value = 0
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

def plot_graph(threadName, lock, chunk_shared, is_playing_audio):
   lock.acquire()
   plt.plot(chunk_shared)
   lock.release()
   plt.show()
   while is_playing_audio == 1:
      print(is_p laying_audio)


def process_data(threadName, lock, chunk_shared, is_playing_audio):
   wf = wave.open ("test.wav", 'rb')
   p = pyaudio.PyAudio()
   chunk = 1024*4

   stream = p.open(
      format=p.get_format_from_width(wf.getsampwidth()),
      channels=wf.getnchannels(),
      rate=wf.getframerate(),
      output=True
      )
   data = wf.readframes(chunk)
   #print(data[:])

   while data != '':
      #stream.write(data)
      data = wf.readframes(chunk)
      #print(data)
      buffer = [x for x in data] #convert byte list to int list
      #print(buffer)
      i = 0
      for elem in buffer:
         lock.acquire()
         chunk_shared[i] = elem
         lock.release()
         i=i+1
      #print(chunk_shared[:])
   stream.close()
   p.terminate

def print_model():
   data = plyfile.PlyData.read('g.ply')['vertex']

   xyz = np.c_[data['x'], data['y'], data['z']]          # Eixos
   rgb = np.c_[data['red'], data['green'], data['blue']] # RGB
   n = np.c_[data['nx'], data['ny'], data['nz']]         # Normais

   # v = pptk.viewer(xyz)
   # v.set(point_size=0.005)
   # v.attributes(rgb / 255., 0.5 * (1 + n))

   # extractedData = rgb[:,[2]]  # gets x axis

   # matrix = 1*[1*[256]]
   # print(matrix)
   # rgb[:,[2]][0] = matrix
   # print(rgb[:,[2]])

   P = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]])

   print("\nP Array:")
   print(P)

   print("\nP[0] Array: selects first row")
   print(P[0])

   print("\nP[:, 0] Array: selects column")
   print(P[:, 0])

   P[0] = [0, 0, 0]
   print("\nP[0] Modified Array")
   print(P[0])

   P[:, 0][0] = 12345678
   print("\nP[:,1] Modified Array")
   print(P)

   print(type(P))

   print("-------------- model rbg array --------------")

   print("RGB Array:")
   print(rgb)

   print("\nRGB[0] Array: selects first row")
   print(rgb[0])

   print("\nP[:, 1] Array: selects green column")
   print(rgb[:, 1])

   rgb[0] = 0
   print("\nRGB[0] Modified Array")
   print(rgb[0])

   # rgb[:, 1] = 0
   print("\nRGB[:,1] Modified Array")
   print(rgb)
   print(type(rgb))


   # size = len(rgb[:,[2]])
   # for x in range(0, size):
   #     rgb[:,[2]][x] = 255;


   # Setup viewer
   v = pptk.viewer(xyz)
   v.set(point_size = 0.007)
   v.attributes(rgb / 255., 0.5 * (1 + n))
   v.set(bg_color = [0, 0, 0, 1])
   v.set(floor_color = [0, 0, 0, 1])
   v.set(show_grid = False)
   v.set(show_axis = False)
   v.set(lookat = [-0.5, 5.50, -8])
   v.set(theta = 0.6)
   v.set(phi = 6)
   v.set(r = 20)

   v.get('view')

   #  (x, y, z, phi, theta, r)
   # Rotates camera
   poses = []
   poses.append([-10, 5, 0, 6 , 0.6, 5])
   poses.append([-5, 5, 0, 6, 0.6, 5])
   poses.append([0, 5, 0, 6, 0.6, 5])
   poses.append([5, 5, 0, 6, 0.6, 5])
   poses.append([10, 5, 0, 6, 0.6, 5])
   poses.append([12, 5, 0, 6, 0.6, 5])
   # play(poses, ts=[], tlim=[-inf, inf], repeat=False, interp='cubic_natural')
   v.play(poses, 2 * np.arange(len(poses)), repeat=True, interp='linear')

   print(type(v))

   #

   # for x in extractedData
   #     element = element % 256 * 1.5


   # print(extractedData)

if __name__ == "__main__":
    lock = multiprocessing.Lock()
    #creating shared memory
    vector = multiprocessing.Array('i', 10)
    chunk_shared = multiprocessing.Array('i', 4096*4);
    is_playing_audio = multiprocessing.Value('i', 0);

    # creating processes
    p1 = multiprocessing.Process(target=print_cube, args=(10, vector, lock))
    p2 = multiprocessing.Process(target=print_model, args=( ))
    p3 = multiprocessing.Process(target=print_time, args=("Thread-3",2))
    p4 = multiprocessing.Process(target=play_sound, args=("Thread-4",2, chunk_shared, lock, is_playing_audio))
    p5 = multiprocessing.Process(target=plot_graph, args=("Thread-5", lock, chunk_shared, is_playing_audio))
    p6 = multiprocessing.Process(target=process_data, args=("Thread-6", lock, chunk_shared, is_playing_audio))
    # starting process
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()

    # wait until the process is finished
    p1.join()
    p2.join()
    p3.join()

    #print(vector[:])
    #print(chunk_shared[:])

    p4.join()
    p5.join()
    p6.join()

    # all the processes finished
    print("Done!")
