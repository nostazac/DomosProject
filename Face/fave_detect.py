import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import pyttsx3
import os

class FaceDetectApp:
    def __init__(self, root, video_source = 0):
        
        self.root = root
        self.root.title("Face Detection")
        self.video_source = video_source
        self.vid = cv2.VideoCapture(self.video_source)
        self.faces = []
        
        self.canvas = tk.Canvas(root)
        self.canvas.pack()
        
        self.btn_start = ttk.Button(root, text = "Start", command = self.start)
        self.btn_start.pack(pady = 10)
        
        self.btn_stop = ttk.Button(root, text = "Stop", command = self.stop)
        self.btn_stop.pack(pady = 10)
        self.btn_stop["state"] = "disabled"
        
        self.btn_export = ttk.Button(root, text="Export Faces", command = self.export_faces)
        self.btn_export.pack(pady = 10)
        self.btn_export['state'] = "disabled"
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.speech_engine = pyttsx3.init()
        
        self.is_running = False
        self.update()
        
    def start(self):
        self.is_running = True
        self.btn_start["state"] = "disabled"
        self.btn_stop["state"] = "enabled"
        self.btn_export["state"] = "disabled"
        
    def stop(self):
        self.is_running = False
        self.btn_start["state"] = "enabled"
        self.btn_stop["state"] = "disabled"
        self.btn_export["state"] = "enabled"
        
    def on_closing(self):
        self.vid.release()
        self.root.destroy()
        
    def update(self):
        if self.is_running:
            ret, frame = self.vid.read()
            
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.faces = self.detect_faces(frame)
                self.display_frame(frame, self.faces)
                
                # if faces:
                #     self.speech_engine.say(f"{len(faces)} faces detected.")
                #     self.speech_engine.runAndWait()
                
        self.root.after(10, self.update)
        
        
    def detect_faces(self, frame):
        
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors= 5)
        
        return faces
    
    def display_frame(self, frame, faces):
        
        if faces is not None:
            
            for (x, y, w, h) in faces:
                
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                
                
        photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
        self.canvas.create_image(0, 0, image = photo, anchor = tk.NW)
        self.canvas.photo = photo
        
    def export_faces(self):
        if not os.path.exists("detected_faces"):
            os.makedirs("detected_faces")
            
        count = 1
        
        for (x, y, w, h) in self.faces:
            face_img = self.vid.read()[1][y:y+h, x:x+w]
            cv2.imwrite(f"detected_faces/face_{count}.jpg", cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB))
            count +=  1
            
        
if __name__ == "__main__":
    
    root = tk.Tk()
    app = FaceDetectApp(root)
    root.mainloop()