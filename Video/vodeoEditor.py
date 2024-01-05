import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip, AudioFileClip
import os

class VideoEditorApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Video Editor")
        
        # Vars
        
        self.video_path = ""
        self.music_path = ""
        self.video_length = 0
        self.fade_duration = 2
        
        # UI elements
        
        def choose_video(self):
            self.video_path = filedialog.askopenfilename(title = "Select Video File", filetypes=[("Video Files", "*.mp4 *.avi")])
            
        def choose_music(self):
            self.music_path = filedialog.askopenfilename(title = "Select Music File", filetypes = [("Aduio Files", "*.mp3")])
            
        def edit_video(self):
            try:
                self.video_length = float(self.length_entry.get())
                self.fade_duration = float(self.fade_entry.get())
                
                video_clip = VideoFileClip(self.video_path)
                music_clip = AudioFileClip(self.music_path)
                edited_clip = video_clip.set_audio(music_clip)
                
                # Trim video to certain length
                edited_clip = edited_clip.subclip(0, self.video_length)
                
                # Add the fading
                edited_clip = edited_clip.fadein(self.fade_duration).fadeout(self.fade_duration)
                
                #output edited video
                
                output_path = os.path.splittext(self.video_path)[0] + ".edited.mp4"
                edited_clip.write_videofile(output_path, codec = "libx264", audio_codec = "aac")
                
            except Exception as e:
                print(f"Error: {e}")
                
        self.video_label = tk.Label(root, text = "Select Video")
        self.video_label.pack()
        
        self.video_button = tk.Button(root, text = "Choose Video", command = self.choose_video)
        self.video_button.pack()
        
        self.music_label = tk.Label(root, text = "Select Music")
        self.music_label.pack()
        
        self.music_button = tk.Button(root, text = "Choose Music", command = self.choose_music )
        self.music_button.pack()
        
        self.length_label = tk.Label(root,  text = "Edit Video Length")
        self.length_label.pack()     
        
        self.length_entry = tk.Entry(root)
        self.length_entry.pack() 
        
        self.fade_label = tk.Label(root, text = "Fade duration (seconds)")
        self.fade_label.pack()
        
        self.fade_entry = tk.Entry(root)
        self.fade_entry.pack()
          
        self.edit_button = tk.Button(root, text = "Edit Video", command =lambda: self.edit_video())
        self.music_button.pack()
                
if __name__ == "__main__":
    root = tk.Tk()
    app = VideoEditorApp(root)
    root.mainloop()