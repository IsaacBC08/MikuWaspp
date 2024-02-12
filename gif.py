import tkinter as tk
from PIL import Image, ImageTk

class AnimatedGifLabel(tk.Label):
    def __init__(self, master, filename, velocidad):
        self.master = master
        self.filename = filename
        self.velocidad = velocidad
        self.gif = self.load_gif(filename)
        super().__init__(master, image=self.gif[0])


    def load_gif(self, filename):
        gif = Image.open(filename)
        frames = []
        try:
            while True:
                gif.seek(len(frames))
                frames.append(ImageTk.PhotoImage(gif.copy()))
        except EOFError:
            pass
        return frames

    def update_animation(self, idx=0):
        idx %= len(self.gif)
        self.config(image=self.gif[idx])
        self.master.after(self.velocidad, lambda: self.update_animation(idx + 1))

#root = tk.Tk()
#root.title("Reproductor de GIF")

 #Define la velocidad deseada en milisegundos
#velocidad = 200  # ajusta este valor según lo desees

#gif_label = AnimatedGifLabel(root, "./img/miku.gif", velocidad)
#gif_label.pack()

#gif_label.update_animation()

#root.mainloop()
