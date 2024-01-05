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
num_bars = 62
x = np.arange(num_bars)
bar_width = 0.8
bar_spacing  = 0.1

bars = ax.bar(x * (bar_width + bar_spacing), np.zeros(num_bars), color = 'yellow', width = bar_width)

#Set the background color to black
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

ax.set_ylim(0, 32768)
ax.set_xlim(0, num_bars)
# Remove the y and x lines
ax.axis('off')

# Fucntion to update matplotlib plot
def update(frame):
     
    audio_data = np.frombuffer(stream.read(CHUNK), dtype = np.int16)
    audio_data = np.abs(audio_data)
    for bar, y in zip(bars, audio_data[:num_bars]):
        bar.set_height(y)
    
    return bars

ani = FuncAnimation(fig, update, blit = True)
plt.show()

# Close the PyAudio stream and terminate PyAudio
stream.stop.stream()
stream.close()
p.terminate()