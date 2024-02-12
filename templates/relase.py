import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
import templates.master as master
from gif import AnimatedGifLabel
import pygame as pg

class App:
    def enviar(self):
        null = ""
        numero = self.numero.get()
        mensaje = self.msj.get()

        if (mensaje != null and numero != null):
            master.enviarMensaje(numero,mensaje,self.ventana)

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Inicar servidor')
        self.ventana.geometry('100x750')
        self.ventana.config(bg='#FF7A48')
        self.ventana.resizable(width=0,height=0)
        utl.centrar(self.ventana, 1368, 760)

        pg.mixer.init()    
        pg.mixer.music.load("./img/relese.mp3")
        pg.mixer.music.play(loops=0)

        frame_logo = tk.Frame(self.ventana, bd=0,width=500,relief=tk.SOLID,padx=10,pady=10,bg='#011F26')
        frame_logo.pack(side="right",expand=tk.NO,fill=tk.BOTH)
        # Define la velocidad deseada en milisegundos
        velocidad = 175  # ajusta este valor según lo desees

        gif_label = AnimatedGifLabel(frame_logo, "./img/miku.gif", velocidad)
        gif_label.config(bg="#94E9F2")
        
        gif_label.update_animation()
        gif_label.place(x=0,y=0,relwidth=1,relheight=1)

        #Frame Form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID,background='#103778')
        frame_form.pack(side='left',expand=tk.YES,fill=tk.BOTH)

        #Frame Form Top
        frame_form_top = tk.Frame(frame_form, height=50, bd=0,relief=tk.SOLID, bg='#011F26')
        frame_form_top.pack(side='top', fill=tk.X)
        title = tk.Label(frame_form_top, text="Comienza a escribir tu mensaje!", font=('times', 20), fg='#161F30',bg='#6C7A8C',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)
        frame_form_separ = tk.Frame(frame_form,height=12,bd=0,relief=tk.SOLID,bg='#011F26')
        frame_form_separ.pack(expand=tk.NO, fill=tk.BOTH)
        
        #Frame Form Fill
        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#385DA6')
        frame_form_fill.pack(side='bottom',expand=tk.YES, fill=tk.BOTH)

        #Fill Labels
        etiqueta_numero = tk.Label(frame_form_fill, text="Número", font=('times', 14), fg='white',bg='#5A90BF', anchor='w')
        etiqueta_numero.pack(fill=tk.X,padx=20,pady=5)

        self.numero = ttk.Entry(frame_form_fill,font=('times', 14))
        self.numero.pack(fill=tk.X, padx=20, pady=10)                
                
        etiqueta_msj= tk.Label(frame_form_fill, text="Mensaje", font=('times', 14), fg='white',bg='#5A90BF', anchor='w')
        etiqueta_msj.pack(fill=tk.X,padx=20,pady=5)
        
        self.msj = ttk.Entry(frame_form_fill,font=('times', 14))
        self.msj.pack(fill=tk.X, padx=20, pady=20)


        inicio = tk.Button(frame_form_fill, text="Enviar Mensaje",font=('times', 18, BOLD), bd=0, bg='#171559', fg='#ffffff',command=self.enviar)
        inicio.pack(fill=tk.X, padx=25, pady=25)
        
        inicio.bind("<Return>", (lambda event: self.enviar()))


        self.ventana.mainloop()