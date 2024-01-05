import tkinter as tk

from PIL import Image, ImageDraw, ImageFilter ,ImageTk

class ImageEditorApp(tk.Frame):
    
    def __init__(self, master):
        
        tk.Frame.__init__(self, master)
        
        # load the images
        self.image = Image.open("domo1.jpg")
        
        #create a new image object
        self.new_image = Image.new("RGB", (self.image.width, self.image.height))
        
        # Remove blemishes
        self.remove_blemishes()
        
        # Apply style
        self.apply_style()
        
        # Create a tkinter image object
        self.tkinter_image = ImageTk.PhotoImage(self.new_image)
        
        # Display the new image
        
        self.image_label = tk.Label(self, image = self.tkinter_image)
        self.image_label.pack()
        
    def composite_image(self):
        
        # Paste the image into the new image   
        self.new_image.paste(self.image,(0, 0))
        
    def remove_blemishes(self):
        
        # Get the pixels of the image
        self.pixel_values = self.new_image.getpixel()
        
        for x in range(self.image.width):
            for y in range(self.image.height):
                pixel_value = self.pixel_values[x ,y]

                if pixel_value > 200:
                    self.pixel_values[x, y] = (self.pixels_values[x - 1, y] + self.pixels_values[x + 1, y] + self.pixel_values[x, y - 1] + self.pixel_values[x, y + 1]) / 4

            
            # Save the edited image
            
            self.new_image.putpixel(self.pixel_values)
    
    def apply_style(self):
        
        # Apply a Gaussian blur to the image
        self.new_image = self.new_image.filter(ImageFilter.GaussianBlur(radius=3))
        
    def save_image(self):
        
        self.new_image.save("edited_image.jpg")
        
if __name__ == "__main__":
    
    root = tk.Tk()
    app = ImageEditorApp(root)
    app.mainloop()