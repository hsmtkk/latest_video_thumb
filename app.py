import tkinter as tk
from PIL import Image, ImageTk
import latest_video_thumb

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.channel_name = tk.Entry(self)
        self.channel_name.pack()

        self.get_thumb = tk.Button(self)
        self.get_thumb["text"] = "Get thumbnail"
        self.get_thumb["command"] = self.get_thumbnail
        self.get_thumb.pack()

        image = Image.open("thumb.jpg")
        photo = ImageTk.PhotoImage(image)
        self.canvas = tk.Label(self, width=480, height=360, image=photo)
        self.canvas.image = photo
        self.canvas.pack()

    def get_thumbnail(self):
        self.canvas.pack_forget()
        channel_name = self.channel_name.get()
        latest_video_thumb.youtube_thumb('AIzaSyAJJjMoXQWpuJob_d89nqb9QMotCcj-bOg', channel_name, 'thumb.jpg')
        image = Image.open("thumb.jpg")        
        photo = ImageTk.PhotoImage(image)
        self.canvas = tk.Label(self, width=480, height=360, image=photo)
        self.canvas.image = photo
        self.canvas.pack()

root = tk.Tk()
app = Application(master=root)
app.mainloop()