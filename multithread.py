#!/usr/bin/python

import _thread as thread
import time
#to play the sound
import pyaudio
import wave

#to plot the sound
from numpy.fft import *
from numpy import log10, sqrt, array, zeros, ones, multiply
import numpy as np

import math
import wave
import struct
import matplotlib.pyplot as plt
from scipy.io.wavfile import write



# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 15:
      time.sleep(delay)
      count += 1
      string = threadName + ':' + time.ctime(time.time())
      print(string)
      #print"%s: %s" % ( threadName, time.ctime(time.time()) )

# Define function to play the sound on a thread
def play_sound( threadName, delay):
   wf = wave.open ("test.wav", 'rb')
   p = pyaudio.PyAudio()
   chunk = 1024

   stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),rate=wf.getframerate(), output=True)
   data = wf.readframes(chunk)

   while data != '':
   	stream.write(data)
   	data = wf.readframes(chunk)

   stream.close()
   p.terminate

def get_samples(file):

    waveFile = wave.open(file, 'r')
    samples = []

    # Gets total number of frames
    length = waveFile.getnframes()

    # Read them into the frames array
    for i in range(0,length):
        waveData = waveFile.readframes(1)
        data = struct.unpack("%ih"%2, waveData)

        # After unpacking, each data array here is actually an array of ints
        # The length of the array depends on the number of channels you have

        # Drop to mono channel
        samples.append(int(data[0]))

    samples = array(samples)
    return samples

# Plot the sound on a thread
def plot_sound( threadName, delay):
   # Generates array of samples reading audio file
   samples = get_samples('maybe-next-time.wav')
   plt.plot(samples)
   plt.show()

   # Transform array of data into playable audio
   scaled = np.int16(samples/np.max(np.abs(samples)) * 32767)
   write('test.wav', 44100, scaled)

# Create two threads as follows
try:
   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   thread.start_new_thread( play_sound, ("Thread-2", 4, ) )
   #thread.start_new_thread( plot_sound, ("Thread-3", 6, ) )
except:
   print("Error: unable to start thread")

while 1:
   pass
