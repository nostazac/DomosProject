import tkinter as tk
from tkinter import ttk, filedialog
import pyttsx3
from pygame import mixer

mixer.init()
def play_ringtone():
    text_to_speak = entry.get()
    engine = pyttsx3.init()
    
    speed = speed_slider.get()
    
    engine.setProperty('rate', speed)
    engine.save_to_file(text_to_speak, 'temporary_ringtone.mp3')
    engine.runAndWait()
    
    mixer.music.load('temporary_ringtone.mp3')
    mixer.music.play()

def create_ringtone():
    text_to_speak = entry.get()
    engine = pyttsx3.init()
    
    speed = speed_slider.get()
    
    engine.setProperty('rate', speed)
    engine.say(text_to_speak)
    
    file_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                             filetypes = [("MP3 files", ".mp3")],
                                             title = "Save Ringtone As")
    
    if file_path:
        
        engine.save_to_file(text_to_speak, file_path)
        engine.runAndWait()
        status_label.config(text = 'Ringtone  created successfully!')
        entry.delete(0, tk.END)
    
    
app = tk.Tk()
app.title("Ringtone Creator")


style = ttk.Style()
style.configure("TFrame", background = "#FFD700")
style.configure("TFrame", background = "#FF6984")
style.configure("TFrame", background = "#FFD700", font = ("Arial", 12))

frame = ttk.Frame(app, padding = '10')
frame.grid(row = 10, column = 0, sticky=(tk.W, tk.E, tk.N, tk.S))

entry = ttk.Entry(frame, width = 40)
entry.grid(row = 0, column = 0, pady = 10, padx = 10)

speed_label = ttk.Label(frame, text="Speed:")
speed_label.grid(row = 1, column = 1, pady = 6)

speed_slider = ttk.Scale(frame, from_= 50, to = 300, orient = tk.HORIZONTAL, length = 200)
speed_slider.set(150)
speed_slider.grid(row = 1, column = 2, padx = 10, pady = 5)

play_button = ttk.Button(frame, text = "Pl ay", command = play_ringtone)
play_button.grid(row = 3, column=0, pady = 10)

create_button = ttk.Button(frame, text="Create Ringtone", command = create_ringtone)
create_button.grid(row = 1, column = 0, pady = 10)

status_label = ttk.Label(frame, text="", foreground = "#008000")
status_label.grid(row = 2, column = 0, pady = 10)


mixer.init()
app.mainloop()