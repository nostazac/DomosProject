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
x = np.arange(0, CHUNK)
bars = ax.bar(x, np.zeros(CHUNK), color = 'aquamarine')

#Set the background color to black
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

ax.set_ylim(-32768, 32768)
ax.set_xlim(0, CHUNK)
# Remove the y and x lines
ax.axis('off')

# Fucntion to update matplotlib plot
def update(frame):
    
    audio_data = np.frombuffer(stream.read(CHUNK), dtype = np.int16)
    
    for bar, y in zip(bars, audio_data):
        bar.set_height(y)
    
    return bars

ani = FuncAnimation(fig, update, blit = True)
plt.show()

# Close the PyAudio stream and terminate PyAudio
stream.stop.stream()
stream.close()
p.terminate()