import tkinter as tk
from tkinter.font import BOLD
from tkinter.ttk import *
import util.generic as utl
import pywhatkit
import datetime as dt
import pyautogui as pag
import time as t



class splash_screen():
    def iniciar(self):
        GB = 100
        carga = 0
        cargando = tk.Label(text="Cargando...",bg="#9AEBA3",fg="#000000",font=('times', 16))
        cargando.pack(side='top',expand=tk.NO, fill=tk.BOTH)
            
        while(carga < GB):
            t.sleep(0.1)
            print("Cargando... ", carga, "%")
            self.barra['value'] += 2
            carga += 2
            self.ventana.update_idletasks()
        t.sleep(0.8)
        self.ventana.destroy()
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Servidor de Whatsapp')
        w = self.ventana.winfo_screenwidth()
        h = self.ventana.winfo_screenheight()
        print(w, " ", h)
        self.ventana.geometry("%dx%d+0+0" % (w,h))
        self.ventana.config(bg='#45C4B0')
        self.ventana.resizable(width=0,height=0)
        logo = utl.imagen('./img/logo.png', (200, 200))
        label = tk.Label(self.ventana, image=logo, bg='#9AEBA3')
        label.place(x=0,y=0,relwidth=1,relheight=1)

        self.barra = Progressbar(self.ventana, orient="horizontal",length=300)
        self.barra.pack(padx=30,pady=150,expand=tk.NO, side="bottom",fill=tk.BOTH)
        
        boton = tk.Button(self.ventana,text="Iniciar",command=self.iniciar,font=('times', 18, BOLD), bd=0, bg='#012030', fg='#ffffff')
        boton.place(x=600, y=640, relheight=0.1,relwidth=0.1)
        self.ventana.mainloop()


def enviarMensaje(Numero:str,mensaje:str, ventana):
    print(Numero, mensaje)
    hora_pc = dt.datetime.now()
    hora_sin_formato = hora_pc.strftime("%H:%M")
    hora_exacta = hora_sin_formato[slice(0,2)]
    print(hora_exacta)
    minuto_sin_formato = slice(3,5)
    minuto_con_formato = int(hora_sin_formato[minuto_sin_formato]) + 1
    minuto_exacto = minuto_con_formato
    print(minuto_exacto)
    ventana.update_idletasks()
    pywhatkit.sendwhatmsg(str(Numero), str(mensaje), int(hora_exacta), int(minuto_exacto), 10)
    t.sleep(1)
    pag.press("enter")
    print("Enviado")