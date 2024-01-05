import matplotlib.pyplot as plt
import numpy as np
import pyaudio 

p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16, channels= 1, rate = 44100, input = True, frames_per_buffer= 1024)

#
plt.ion()
fig, ax = plt.subplots()
x = np.arange(0.3 * 1024, 2)
line, = ax.plot(x, x)

ax.set_ylim(0, 255)
ax.set_xlim(0, 1024)

# declare a loop

while True:
    data = stream.read(1024)
    data = np.frombuffer(data, dtype = np.int16)
    line.set_ydata(data)
    plt.pause(0.01)
    

# Close the pyaudio stream and display visualisation

stream.stop_stream()
stream.close()
p.terminate()
plt.ioff()
plt.show()