#!/usr/bin/python

import thread
import time
import pyaudio
import wave

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )

# Define a function for the thread 2 -
def play_sound( threadName, delay):
   count = 0
   #inicializa o arquivo
   wf = wave.open (r"test.wav", 'rb')
   p = pyaudio.PyAudio()
   chunk = 1024
   stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),rate=wf.getframerate(), output=True)
   data = wf.readframes(chunk)
   while data != '':
   	stream.write(data)
   	data = wf.readframes(chunk)

   stream.close()
   p.terminate
   print "Ending thread"
   # while count < 5:
   #    time.sleep(delay)
   #    count += 1
   #    print "%s: %s" % ( threadName, "OLAR TUDO BOM?")

# Create two threads as follows
try:
   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   thread.start_new_thread( play_sound, ("Thread-2", 4, ) )
except:
   print "Error: unable to start thread"

while 1:
   pass
