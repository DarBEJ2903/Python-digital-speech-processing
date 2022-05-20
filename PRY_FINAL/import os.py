from ast import While
from calendar import c
import os
from tracemalloc import start
from clase_grabacion import AudioHelp
from github_grabar import aud
import threading
import time
from tkinter import END
from tkinter import *
from tkinter  import messagebox
from clase_starend_work import prin_fin_work
from correlation import Correlation
from pydub.playback import play
import serial
import pandas as pd
from scipy.io import wavfile
from pydub import AudioSegment
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pylab import mpl

ventana=Tk()
variable_ini_grabacion = 0


ser = serial.Serial(
	port='COM5',\
	baudrate=9600,\
	parity=serial.PARITY_NONE,\
	stopbits=serial.STOPBITS_ONE,\
	bytesize=serial.EIGHTBITS,\
	timeout=0)



class MainAudio(threading.Thread):
    """ Clase para probar las funcionalidades del plugin AudioHelp. """
    
    

    def __init__(self):

        global variable_ini_grabacion
        self.vector_ref = ["cocina","patio","sala","cuarto"]
        self.work_reference =[]
        a = variable_ini_grabacion
        self.audio_help = AudioHelp()
        self.corr = Correlation([])
        self.test_recording(a)
       
        

    def test_recording(self,a):
        """ 
            Función de ejecución secuencial para probar grabación, 
            reconocimiento de audio a texto y reproducción de audio. 
        """
        while 1:
            
            if variable_ini_grabacion == 1:
                
                sonido1= None
                self.ad = aud()
                correlacion = []
                self.Pincipio_fin = prin_fin_work()
                palabras = self.Pincipio_fin.reproducir()
                print("reproduciendo palabra 1")
                play(palabras[0])
                time.sleep(0.3)
                print("reproduciendo palabra 2")
                play(palabras[1])
                time.sleep(0.3)
                palabras[0] = palabras[0].get_array_of_samples()
                palabras[0] = np.array(palabras[0])
                
                palabras[1] = palabras[1].get_array_of_samples()
                palabras[1] = np.array(palabras[1])


                for n in range (0,2,1):
                    
                    for m in range (0,5,1):
                        
                        works = AudioSegment.from_file(f'./PRY_FINAL/work_{self.vector_ref[n]}{m + 1}.wav')
                        works = works.get_array_of_samples()
                        self.work_reference.append(works)
                        
                        
                for n in range (0,len(self.work_reference),1):

                    tamaño1 = len(self.work_reference[n])
                    tamaño2 = len(palabras[0])
                    l = abs(tamaño1-tamaño2)
                    c = np.zeros(l)
                    if tamaño1 > tamaño2: 
                        palabras[0] = np.append(palabras[0], c)
                    else:
                        self.work_reference[n] = np.append(self.work_reference[n], c)

                    correlacion.append(cross_corr(palabras[0], self.work_reference[n]))
                    #print(f"Cross Correlation a,b: {cross_corr(palabras[0], self.work_reference[n])}")
            
               
                indice_maximo = correlacion.index(np.max(correlacion))
             
                print(indice_maximo)

                if indice_maximo == 0:
                    print("Es cocina")
                elif indice_maximo == 1:
                    print("Es patio")
                else:    
                    pass
"""                elif (indice_maximo>= 10) and (indice_maximo<15):
                    print("Es sala")
                elif (indice_maximo>= 15) and (indice_maximo<20):
                    print("Es cuarto") """
                
            
   
            

         
"""                self.corr.__init__(palabras,"Work")
                data_frame = self.corr.dataTreatment()
                #self.corr.plotImages(True)

                for n in range (0,4,1):
                    
                    for m in range (0,5,1):
                        works = AudioSegment.from_file(f'./PRY_FINAL/work_{self.vector_ref[n]}{m + 1}.wav')
                        self.work_reference.append(works)

                   # work_patio = AudioSegment.from_file(f'./PRY_FINAL/work_patio{n + 1}.wav')
                   # work_cocina = work_cocina/max(work_cocina)
                   

                self.corr.__init__(self.work_reference,"referencia_cocina")
                df_referencia = self.corr.dataTreatment()
                #self.corr.plotImages(True)
                df_join = pd.concat([data_frame,df_referencia],axis=1)
                df_join = df_join.fillna(0)
                correlacion = df_join.corr()
                print(abs(correlacion.iloc[0:2,::]))
                correlacion = correlacion.iloc[0:2,::]
                correlacion = correlacion.to_numpy()          
                max_valor_fw = np.max(correlacion[0][2::])
                print (np.around(abs(correlacion),2))
                print(max_valor_fw)
                for n in range (2,22,1):
                    if correlacion[0][n]== max_valor_fw:
                        if (n >= 2 ) and (n<7):
                            print("Es cocina")
                        elif (n>= 7) and (n<12) :
                            print("Es patio")
                        elif (n>=12) and (n<17):
                            print("Es sala")
                        elif (n>= 17) and (n<22):
                            print("Es cuarto")
                        else:
                     pass

                        
                    else: 
                        pass
                
                self.work_reference = []
"""             
            
def cross_corr(set1, set2):

        set1 = np.array(set1)
        set2 = np.array(set2)
        return np.sum(set1 * set2)          


def imprimir():
    global variable_ini_grabacion
    variable_ini_grabacion = 1
    print("hola\r\n")


ventana.geometry("400x400+0+0")
ventana.title("aplicacion de grabacion")
Button(ventana, text="GRABAR",command = imprimir).place(x = 50 , y =200)

class com_serial(threading.Thread):

    def __init__(self):
        
        self.enviar()
    
    def enviar(self):

        while 1:
            ser.write(b'k')


if __name__ == '__main__':

  
    hilo2 = threading.Thread(target=MainAudio)
#    hilo3 = threading.Thread(target=com_serial)

    hilo2.start()
#    hilo3.start()

ventana.mainloop()