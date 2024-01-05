import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoClip, AudioClip,VideoFileClip,AudioFileClip
import os


def choose_video():
    video_path = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video Files", "*.mp4 *.avi")])
    return video_path

def choose_music():
    music_path = filedialog.askopenfilename(title = "Select Music File", filetypes=[("Audio Files", "*.mp3")])
    return music_path

def trim_music(music_path, start_time, end_time):
    
    try:
        music_clip = AudioFileClip(music_path)
        trimmed_music = music_clip.subclip(start_time, end_time)
        return trimmed_music
    
    except Exception as e:
        print(f"Error: {e}")
        return  None

def play_trimmed_music(trimmed_music):
    
    if trimmed_music:
        trimmed_music.preview(fps = 44100)
    else:
        print("Please trim the music first.")
        
def bind_music_to_video(video_path, trimmed_music):
    
    try:
        video_clip = VideoFileClip(video_path)
        
        if trimmed_music:
            video_clip = video_clip.set_audio(trimmed_music)
            output_path = os.path.splitext(video_path)[0] - "_with_music.mp4"
            video_clip.write_videofile(output_path, codec="libx264", audio_codec = "aac")
            
            print("Video successfully bound with background music")
            
        else:
            print("Please trim and choose music before binding.")
            
    except Exception as e:
        
        print(f"Error: {e}")
        
        
def play_video_with_music(video_path, trimmed_music):
    
    try:
        video_clip = VideoFileClip(video_path)
        music_clip = AudioFileClip(trimmed_music)
        final_clip = video_clip.set_audio(music_clip)
        final_clip.preview()
        
    except Exception as e:
        
        print(f"Error: {e}")
        
def main():
    root = tk.Tk()
    root.title("Video Editor")
    
    video_path = ""
    music_path = ""
    trimmed_music = None
    
    video_label = tk.Label(root, text="select video")
    video_label.pack()
    
    video_button = tk.Button(root, text  = "choose video", command=choose_video)
    video_button.pack()
    
    music_label = tk.Label(root, text="select music")
    music_label.pack()
    
    music_button = tk.Button(root, text  = "choose video", command=choose_music)
    music_button.pack()
    
    trim_button = tk.Button(root, text  = "trim Music", command=trim_music(music_path, 0, 10))
    trim_button.pack()
    
    play_button = tk.Button(root, text  = "Play trimmed music", command=play_trimmed_music(trimmed_music))
    play_button.pack()
    
    bind_button = tk.Button(root, text  = "Bind music to video", command= bind_music_to_video(video_path, trimmed_music))
    bind_button.pack()
    
    play_video_button = tk.Button(root, text  = "Play video with background music", command = play_video_with_music(video_path,trimmed_music))
    play_video_button.pack()
    
    root.mainloop()
    
    
if __name__ == "__main__":
    main()