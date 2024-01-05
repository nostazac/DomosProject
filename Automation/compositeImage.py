import tkinter as tk
from tkinter import * 
from PIL import Image, ImageTk

class CompositeImageApp(tk.Frame):
    def __init__(self, master):
        
        tk.Frame.__init__(self, master)
        
        
        #load the images to be combined
        self.image1 = Image.open("domo1.jpg")
        self.image2 = Image.open("composite_image.jpg")
        
        #create a new Image object
        self.new_image = Image.new("RGB", (self.image1.width, self.image1.height))
        
        #paste the images into the new image
        self.new_image.paste(self.image1, (0,0))
        self.new_image.paste(self.image2,(0, self.image2.height))
        #save the new image
        
        self.new_image.save("composite_image1.jpg")
        
         # Create a tkinter image object
        self.tkinter_image = ImageTk.PhotoImage(Image.open("composite_image1.jpg"))
        # Display the image
        self.image_label = tk.Label(self, image = self.tkinter_image)
        self.image_label.pack()
        

root = tk.Tk()
frame = Frame(root, width = 600, height = 400)
frame.pack()

frame.place(anchor = 'center', relx = 0.5, rely = 0.5)
app = CompositeImageApp(root)
root.geometry("700x500")
app.mainloop()
