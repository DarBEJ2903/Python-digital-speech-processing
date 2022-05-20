import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

def cross_corr(set1, set2):
    return np.sum(set1 * set2)


rate, data = wavfile.read('PRY_FINAL/recorte2.wav')
rate, data2 = wavfile.read('PRY_FINAL/work_patio1.wav')

data = np.array(data)
data2 = np.array(data2)

tamaño1 = len(data)
tamaño2 = len(data2)
l = abs(tamaño1-tamaño2)
c = np.zeros(l)
if tamaño2 > tamaño1: 
    data = np.append(data,c)
else:
    data2 = np.append(data2,c)

amplitud = np.max(data)
data = data/amplitud
data2 = data2/amplitud

tamaño1 = len(data)
tamaño2 = len(data2)
plt.figure(1)
plt.plot(data)
plt.figure(2)
plt.plot(data2)
plt.show()
        
print(f"Cross Correlation a,b: {cross_corr(data, data)}")
print(f"Cross Correlation a,c: {cross_corr(data, data2)}")
#print(f"Cross Correlation b,c: {cross_corr(b, c)}")