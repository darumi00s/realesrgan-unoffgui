import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image

window = Tk()

class UpScaler(tk.Frame):

    def __init__(self, window):
        super().__init__(window)
        self.init_ui()

    def init_ui(self):
        self.pack()
        self.canvas = Canvas(window, bg="#ffffff", height=350, width=700, bd=0, highlightthickness=0, relief="ridge")
        self.canvas.place(x=0, y=0)
        v = StringVar(window, value='please, set me first:(')
        self.background_img = PhotoImage(file=f"./src/background.png")
        self.background = self.canvas.create_image(412.0, 118.0, image=self.background_img)
        self.img0 = PhotoImage(file=f"./src/img0.png")
        self.b0 = Button(image=self.img0, borderwidth=0, highlightthickness=0, command=self.open_image, relief="flat")
        self.b0.place(x = 357, y = 154, width = 140, height = 43) 
        self.label1 = self.canvas.create_text(580.0, 185.0, text='no file chosen.', fill="#ffffff", font=("Gotham-Medium", int(14.0)))
        self.img1 = PhotoImage(file=f"./src/img1.png")
        self.b1 = Button(image=self.img1,borderwidth=0,highlightthickness=0,command=self.up_image,relief="flat")
        self.b1.place(x=464, y=295, width=123, height=42)
        self.img2 = PhotoImage(file=f"./src/img2.png")
        self.b2 = Button(image=self.img2,borderwidth=0,highlightthickness=0,command=self.app_info,relief="flat")
        self.b2.place(x=584, y=203, width=68, height=35)
        self.txt1 = PhotoImage(file=f"./src/img_textBox0.png")
        self.t1a = self.canvas.create_image(513.0, 262.5, image =self.txt1)
        self.t1b = Entry(bd = 0, bg = "#ffffff", highlightthickness = 0, textvariable=v)
        self.t1b.place(x = 379.0, y = 244,width = 268.0, height = 35)
        self.t1b.bind("<1>", self.output_loc)

    def open_image(self):
        self.filename = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpeg *.jpg *.png"), ("All files", "*.*")])
        self.filetext = os.path.split(self.filename)[1]
        self.canvas.itemconfig(self.label1, text=self.filetext)

    def output_loc(self, event):
        self.output_path = filedialog.askdirectory()
        self.t1b.delete(0, END)
        self.t1b.insert(0, self.output_path)

    def app_info(self): 
        messagebox.showinfo(title="Real-ESRGAN GUI", message='Settings are automatically for artwork/anime optimization, default upscale ratio is 4 and models default is realesrgan-x4plus-anime. \n\nThis is unofficial gui btw :"v')
    
    def up_image(self):
        self.fileout = os.path.split(self.filename)[1]
        try:
            outputname =  self.output_path + 'upscaled-' + self.fileout
            os.system(f'realesrgan -i "{self.filename}" -o "{outputname}" -n realesrgan-x4plus-anime')
            messagebox.showinfo(title="Real-ESRGAN GUI",
                            message=f"Image {self.fileout} Has Upscaled Successfully in {outputname}, Enjoy!")
            showimg = Image.open(f'{outputname}')
            showimg.show()
        except AttributeError:
            messagebox.showerror(title="Real-ESRGAN GUI: Exception", message="Please, set output directory first!")
            
window.geometry("700x350")
window.configure(bg = "#ffffff")
window.title('Real-ESRGAN GUI')
window.iconbitmap('./src/icon.ico')
window.resizable(False, False)

envipath = os.environ['PATH']
prog = 'realesrgan'
if prog in envipath:
    gui = UpScaler(window)
else:
    messagebox.showerror(title="Real-ESRGAN GUI",
                         message="You must download Real-ESRGAN & set to Environment Path!")
    window.destroy()

window.mainloop()