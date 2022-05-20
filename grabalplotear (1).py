import pyaudio
import scipy.io.wavfile as wavfile
import matplotlib.pylab as plt
import wave


chunk=1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
RECORD_SECONDS = 2
samples = (RATE/1024)*RECORD_SECONDS

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,channels=CHANNELS,rate =RATE,input=True,frames_per_buffer=chunk)
stream1 = p.open(format=FORMAT,channels=CHANNELS,rate =RATE,output=True,frames_per_buffer=chunk)

print ("grabando")

arreglo = []
for i in range(0, int(samples)):
        data = stream.read(chunk)
        arreglo.append(data)

stream.stop_stream()
stream.close()
stream1.stop_stream()
stream1.close()


wf = wave.open('ANDRES1.wav', 'wb')
wf.setnchannels(CHANNELS)
wf.setframerate(RATE)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.writeframes(b''.join(arreglo))
wf.close()

print ("fin")




rate, data = wavfile.read("ANDRES1.wav")

print (rate)

plt.figure(1)
plt.plot(data)
#plt.show()

c=2*data


plt.figure(2)
plt.plot(c)
plt.show()


wavfile.write("ANDRES2.wav", RATE, c)



print ("done")
