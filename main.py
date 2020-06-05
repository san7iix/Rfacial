from tkinter import *


#Funciones
def empezar():
    etiqueta_estado.configure(text="Estado: En ejecución")

def detener():
    etiqueta_estado.configure(text="Estado: En pausa")
#Configuración de ventana    
window = Tk()
window.geometry('800x600')
window.title("Reconocimiento facial")
# Etiquetas
etiqueta_video = Label(window, text="Video")
etiqueta_video.grid(column=0,row=0)
# Etiqueta de estado
etiqueta_estado = Label(window, text="Estado: En pausa")
etiqueta_estado.grid(column=0,row=1)
# Botones
btn_comenzar = Button(window, text="Comenzar",command=empezar)
btn_stop = Button(window, text="Detener",command=detener)
btn_comenzar.grid(column=0, row=2)
btn_stop.grid(column=2, row=2)



window.mainloop()


