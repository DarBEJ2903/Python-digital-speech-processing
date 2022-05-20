from doctest import master
from turtle import down, left
import tkinter                  
import pyaudio
import sys
import numpy as np
import wave
import scipy.io.wavfile as wavfile
from matplotlib.pylab import mpl
from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.pyplot import step
from tkinter import filedialog

import matplotlib.pyplot as plt
import time

ventana=Tk()
ventana.geometry("1080x900+0+0")
ventana.title("aplicacion de grabacion")

fig,ax = plt.subplots(figsize=(10,4),dpi=100)
canvas=FigureCanvasTkAgg(fig,master = ventana)
canvas.get_tk_widget().pack



ventana.mainloop()


















 