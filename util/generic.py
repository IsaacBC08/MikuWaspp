from PIL import Image, ImageTk

def imagen(ruta:str, px:int):
    return ImageTk.PhotoImage(Image.open(ruta).resize(px, Image.ANTIALIAS))

def centrar(ventana, app_ancho:int, app_largo:int):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_largo = ventana.winfo_screenheight()
    x = int((pantalla_ancho / 2)  - (app_ancho / 2))
    y = int((pantalla_largo / 2 ) - (app_largo / 2))
    return ventana.geometry(f"{app_ancho}x{app_largo}+{x}+{y}")