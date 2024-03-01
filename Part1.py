from scipy import fft
from math import pi
from numpy import arange, cos, abs
import matplotlib.pyplot as plt

A=4
N=250
fi=pi/8
k=arange(0,1023)

s=(2*pi*k)/N
print(s)
x1=A*cos(s+fi)
print("Функция сигнала:")
print(x1)
y=fft.fft(x1)
print("Прямое преобразование Фурье:")
print(y)
F=fft.ifft(y)
print("Обратное преобразование Фурье:")
print(F)
f=arange(0,len(y))/len(y)
print("Вектор частот:")
print(f)

#Вывод граффиков
plt.figure(figsize=(12,8))

plt.subplot(3,1,1)
plt.plot(k,x1,label='Исходный сигнал')
plt.title('Исходный сигнал')
plt.xlabel('k')
plt.ylabel('x1')
plt.legend()

plt.subplot(3,1,2)
plt.plot(k,abs(y),label='Прямое преобразование Фурье')
plt.title('Прямое преобразование Фурье')
plt.xlabel('k')
plt.ylabel('y')
plt.legend()

plt.subplot(3,1,3)
plt.plot(k,F,label='Обратное преобразование Фурье')
plt.title('Обратное преобразование Фурье')
plt.xlabel('k')
plt.ylabel('F')
plt.legend()

plt.show()
