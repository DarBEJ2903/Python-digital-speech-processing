import threading
from tkinter import END
from tkinter import *
from tkinter  import messagebox
import clase_grabacion
import numpy
import os

boton_grabar = 0

def interfaz():
    global boton_grabar
    def var_grabar():
        print("hola\r\n")

    ventana=Tk()
    ventana.geometry("1080x900+0+0")
    ventana.title("aplicacion de grabacion")
    Button(ventana, text="GRABAR",command = var_grabar() ).place(x = 50 , y =400)
    ventana.mainloop()

def grabacion():
    gr = clase_grabacion.AudioHelp()
    
    def empezar():
        """ 
            Función de ejecución secuencial para probar grabación, 
            reconocimiento de audio a texto y reproducción de audio. 
        """
        print("Grabación de 5 segundos de prueba ...")
        t_stop = threading.Timer(5.0,stop_audio()) # En 5 segundos ejecuta la función stop_audio
        t_stop.start()
        start_audio() # Comerzar a grabar el audio
        play_audio() # Reproducir audio guardado

    def get_url_save():
        """ Función de la ruta absoluta en donde se ubicará el audio nuevo o existente. """
        return os.path.dirname(os.path.abspath(__file__)) + "/PRY_FINAL/test_audio.wav"    

    def final_audio():
        """ 
            Función llamada en start_audio dentro de la variable callback_final, 
            que se ejecuta cuando el audio ha sido guardado en la ruta especificada. 
        """
        print("Audio guardado!! ................")

    def refresh_window():
        """ 
            Función llamada en start_audio dentro de la variable callback_refresh,
            que se ejecuta mientras el audio continue en estado de grabación.
        """
        print("Grabando ........................")

    def play_audio():
        """ Función para reproducir audio. """
        print("Reproducir audio existente ......")
        gr.play_audio(
            url_path= get_url_save()
        )

    
    def stop_audio():
        """ Función para detener el audio. """
        print("Detener audio ...................")
        gr.stop_recording()

    def start_audio():
        """ Función para comenzar a grabar. """
        print("Comenzar grabación ..............")
        gr.start_recording(
            url_path= get_url_save(), 
            callback_refresh= refresh_window,
            callback_final=final_audio
        )
    empezar()


hilo1 = threading.Thread(target=interfaz)
hilo2 = threading.Thread(target=grabacion)

hilo1.start()
hilo2.start()
