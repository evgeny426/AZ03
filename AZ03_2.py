# Задание 2
# Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`.

import matplotlib.pyplot as plt
import numpy as np


x = np.random.rand(5)
y = np.random.rand(5)
plt.scatter(x, y)
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('Диаграмма рассеяния двух наборов случайных данных')
plt.show()