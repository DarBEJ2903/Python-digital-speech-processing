import threading
import time
import sys
from tkinter import END
import serial



ser = serial.Serial(
	port='COM5',\
	baudrate=9600,\
	parity=serial.PARITY_NONE,\
	stopbits=serial.STOPBITS_ONE,\
	bytesize=serial.EIGHTBITS,\
	timeout=0)

def funcion1():
    ser.write(b"hola\r\n")

   

class mi_hilo2(threading.Thread):
    while 1:
	    funcion1()
		time.sleep(1000)
		
		
if __name__ == '__main__':	
	hilo2=mi_hilo2()
	hilo2.start()

