import tkinter as tk
from tkinter import messagebox,font
import PyPDF2
from datetime import datetime

class StudentTracker:
    def __init__ (self, root):
        self.root = root
        self.root.title("Student Day-to0Day Tracker")
        # self.root.geometry("300x400")
        self.activities = []
        self.root.configure(bg = 'yellow')
        
        self.custom_font = font.Font(family = "Times New Roman", size = 12, weight = "bold")
        
        self.label = tk.Label(root, text="Today's Activities: ",font = self.custom_font, bg = 'yellow',fg="Blue")
        self.label.pack(padx = 10, pady = 5)
        
        self.date_label = tk.Label(root, text=f" Date: {datetime.now().strftime('%Y-%m-%d')}",  font = self.custom_font,bg = 'yellow',borderwidth=3)
        self.date_label.pack(pady=10)
        
        self.activities_text = tk.Text(root, height = 5, width=30)
        self.activities_text.pack(pady = 10)
        
        self.button_frame = tk.Frame(root, bg = "Black")
        self.button_frame.pack(fill = tk.BOTH, expand=True,)
        
        self.add_button = tk.Button(self.button_frame, text  = "Add Activity", command = self.add_activity, bg = '#4CAF50', fg = 'white', relief = tk.RAISED, borderwidth=3)
        self.add_button.pack(expand = True, fill = tk.BOTH, padx = 20, pady = 10)
        self.add_button.bind("<Enter>", lambda event: self.add_button.config(bg = "darkgreen"))
        self.add_button.bind("<Leave>", lambda event: self.add_button.config(bg = "#4CAF50"))
        
        self.view_button = tk.Button(self.button_frame, text  = "View Activities", command = self.view_activities, bg = '#008CBA', fg = 'white', relief = tk.RAISED, borderwidth=3)
        self.view_button.pack(expand = True, fill = tk.BOTH, padx = 20, pady = 10)
        
        self.view_button.bind("<Enter>", lambda event: self.view_button.config(bg = "#006699"))
        self.view_button.bind("<Leave>", lambda event: self.view_button.config(bg = "#008CBA"))
        
        self.checkbox_frame = tk.Frame(root, bg = 'Yellow')
        self.checkbox_frame.pack(fill = tk.BOTH,padx = 10, pady = 10)
        
        self.upcoming_activities = []
        self.checkboxes = []
        
    def load_activities(self):
        try:
            with open("activities.txt", "r") as file:
                self.activities = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            pass
    
    def save_activities(self):
        with open("activities.txt","w") as file:
            file.write("\n".join(self.activities))
        
        
    def add_activity(self):
        
        activity = self.activities_text.get("1.0", tk.END).strip()
        
        if activity:
            self.activities.append(activity)
            self.save_activities()
            self.add_checkbox(activity)
            messagebox.showinfo("Success", "Activity added successfully!")
            self.activities_text.delete("1.0", tk.END)
            
        else:
            messagebox.showwarning("Warning", "Please enter an activity.")
            
            
    def add_checkbox(self, activity):
        checkbox = tk.Checkbutton(self.checkbox_frame, text=activity)
        checkbox.pack()
        
        self.checkboxes.append(checkbox)
        self.upcoming_activities.append(activity)
        
        
    def view_activities(self):
        
        if not self.activities:
            messagebox.showinfo("No Activities", "No Activities Recorded yet")
    
        else:
            activities_str = "\n".join(self.activities)
            messagebox.showinfo("Activities", f"Today Activities:\n{activities_str}")
    def generate_pdf(self):
        pdf_filename = "upcoming_activities.pdf"
        with open(pdf_filename, 'ab')as pdf_file:
            pdf_writer = PyPDF2.PdfWriter()
            
            pdf_writer.addPage(PyPDF2.PdfReader("Template.pdf").getPage(0))
            
            for checkbox in self.checkboxes:
                if checkbox.instate(['selected']):
                    activity = checkbox.cget("text")
                    pdf_writer.addPage(PyPDF2.PdfReader(self.create_pdf_page(activity)).getPage(0))
                    
            pdf_writer.write(pdf_file)
            
        messagebox.showinfo("PDF Updated", f"{pdf_filename} updated successfully")
        
    def create_pdf_page(self,activity):
        pdf_page = PyPDF2.PdfWriter()
        
        pdf_page.addPage()
        pdf_page.setFont("HElvetica", "12")
        
        pdf_page.drawString(72, 800, f" - {activity}")
        
        return pdf_page
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentTracker(root)
    width = 300
    height = 500
    root.geometry(f"{width}x{height}")
    root.minsize(width, height)
    root.maxsize(width, height)
    
    generate_pdf_button = tk.Button(app.button_frame, text = "Generate PDF", command = app.generate_pdf)
    generate_pdf_button.pack(expand = True, fill = tk.BOTH, padx = 20, pady = 10)
    generate_pdf_button.bind("<Enter>", lambda event: generate_pdf_button.config(bg = "#e64d00"))
    generate_pdf_button.bind("<Leave>", lambda event: generate_pdf_button.config(bg = "#FF5733"))
    
    
    root.mainloop() 