import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Setup audio for audio input
p = pyaudio.PyAudio()

# Audio input settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# Create a Pyaudio stream for audio input
stream = p.open(format = FORMAT,channels = CHANNELS,rate = RATE, input = True, frames_per_buffer = CHUNK )

# Initializee Matplotlib
fig, ax = plt.subplots()
x = np.arange(0, 2 * CHUNK, 2)
line, = ax.plot(x, np.zeros(CHUNK))

ax.set_ylim(-32768, 32768)

# Fucntion to update matplotlib plot
def update(frame):
    
    audio_data = np.frombuffer(stream.read(CHUNK), dtype = np.int16)
    line.set_ydata(audio_data)
    
    return line,
ani = FuncAnimation(fig, update, blit = True)
plt.show()

# Close the PyAudio stream and terminate PyAudio
stream.stop.stream()
stream.close()
p.terminate()