import math as m
import matplotlib.pyplot as plt
import numpy as np

print("Esta gráfica está muy buena!")


z= np.linspace(-10,10,100)
print(z)
y=(z**2)+2
plt.plot(z,y)
plt.show()

# Este codigo genera un grafico con una parabola con 100 puntos entre -10 y 10