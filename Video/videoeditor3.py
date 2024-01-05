import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeVideoClip
from PIL import Image, ImageTk
import cv2
import os

class VideoeditorApp():
    def __init__(self, root):
        
        self.root = root
        self.root.title("Video Editor")
        
        self.video_path = ""
        self.music_path = ""
        self.video_clip  = None
        self.audio_clip = None
        self.video_capture = None
        self.current_frame = None
        # self.trim_start = 0
        # self.trim_end = 0
        
        
        
        def choose_video(self):
            self.video_path = filedialog.askopenfilename(title="Select Video File", filetypes = [("Video Files","*.mp4 *.avi" )])
            self.video_clip = VideoFileClip(self.video_path)
            self.video_capture = cv2.VideoCapture(self.video_path)
            
        def choose_music(self):
            self.music_path = filedialog.askopenfilename(title="Select Audio File", filetypes = [(" Files","*.mp3 *.avi" )])
            self.music_clip = AudioFileClip(self.music_path)
        
        def trim_video(self):
            
            try:
                self.trim_start = float(self.trim_start.get())
                self.trim_end = float(self.trim_entry_end.get())
                self.video_clip = self.video_clip.subclip(self.trim_start, self.trim_end)
                
            except ValueError:
                print("Invalid trim values. Please enter valid numbers.")
                
        # def play_frames(self, frame = None):
            
        #     if frame is None:
        #         frame  = 0
                
        #     if frame < self.video_clip.reader.nframes:
                
        #         self.current_frame = ImageTk.PhotoImage(Image.fromarray(self.video_clip.get_frame(frame)))
        #         self.canvas.create_image(0, 0, anchor = tk.NW, image = self.current_frame)
        #         self.root.after(33, lambda: self.play_frames(frame + 1))
                
        #     else:
        #         self.play_button["state"] = "normal"
            
                
        def play_frames(self):
            
            ret, frame = self.video_capture.read()
            
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = ImageTk.PhotoImage(Image.fromarray(frame))
                self.canvas.create_image(0,0, anchor = tk.NW, image = image)
                self.root.after(33, play_frames(self))
                
            else:
                self.video_capture.release()
                self.play_button["state"] = "normal"
            
        def play_video(self):
            
            if self.video_clip:
                self.play_button["state"] = "disabled"
                play_frames(self)
            else:
                print("Please Choose a video first.")

        def save_video(self):
            
            try:
                if self.audio_clip:
                    video_with_audio = CompositeVideoClip(self.video_clip.set_audio(self.audio_clip))
                    output_path = os.path.splitext(self.video_path)[0] + "_edited.mp4"
                    video_with_audio.write_videofile(output_path, codec="lib264", audio_codec = "acc")
                    print("Video saved successfully")
                    
                else:
                    print("Please choose music before saving.")
                    
            except Exception as e:
                
                print(f"Error: {e}")
                
            
        self.video_label = tk.Label(root, text = "Select Video: ")
        self.video_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        self.video_button = tk.Button(root, text = "Choose Video",command = lambda: choose_video(self))
        self.video_button.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        self.music_label = tk.Label(root, text = "Select Music: ")
        self.music_label.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        self.music_button = tk.Button(root, text = "Chooce Music", command = lambda: choose_music(self))
        self.music_button.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        self.trim_label = tk.Label(root, text = "Trim Video: (in seconds): ")
        self.trim_label.grid(row = 1, column = 0, padx = 10, pady = 10)
        
        self.trim_entry_start = tk.Entry(root)
        self.trim_entry_start.grid(row = 3, column = 0, padx = 10, pady = 10)
        
        self.trim_entry_end = tk.Entry(root)
        self.trim_entry_end.grid(row = 3, column = 1, padx = 10, pady = 10)
        
        self.play_button = tk.Button(root, text = "play Video", command = lambda: play_video(self))
        self.play_button.grid(row = 4, column = 0, padx = 10, pady = 10)
        
        self.save_button = tk.Button(root, text="Save video", command = lambda: save_video(self))
        self.save_button.grid(row = 4, column = 1, padx = 10, pady = 10)
        
        self.canvas = tk.Canvas(root)
        self.canvas.grid(row = 5,column = 3, columnspan= 2)
                
if __name__ == "__main__":
    
    root  = tk.Tk()
    app = VideoeditorApp(root)
    root.mainloop()
                