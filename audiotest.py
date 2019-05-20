#!/usr/bin/python

import pyaudio
import wave



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
