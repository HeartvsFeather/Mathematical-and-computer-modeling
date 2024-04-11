import numpy as np
import matplotlib.pyplot as plot
import random

def f(x): # f(x)
    # return np.sqrt((1 - np.cos(2 * x)) / 2)
    return (x + np.cos(x)) / (np.square(x) + 2 * np.sin(x)) # второй вариант

# a = 0
# b = np.pi
a = 1 # второй вариант
b = np.sqrt(3) # второй вариант
N = 1000

h = (b - a) / N

print(f"\nАналитическое решение: 2")

# метод левых
x_plt = np.arange(a, b - h, h)
res_left = 0
for x in x_plt:
    res_left += f(x) * h
print(f"\nМетодом левых прямоугольников: {res_left}")
print(f"Абсолютная погрешность: {np.abs(2 - res_left)}")
print(f"Относительная погрешность: {(np.abs(2 - res_left)) / 2 * 100} %")

# метод правых
x_plt = np.arange(a + h, b, h)
res_right = 0
for x in x_plt:
    res_right += f(x) * h
print(f"\nМетодом правых прямоугольников: {res_right}")
print(f"Абсолютная погрешность: {np.abs(2 - res_right)}")
print(f"Относительная погрешность: {(np.abs(2 - res_right)) / 2 * 100} %")

#метод трапеций
x_plt = np.arange(a, b - h, h)
res_trap = 0
for x in x_plt:
    res_trap += (f(x) + f(x + h)) / 2 * h
print(f"\nМетодом трапеций: {res_trap}")
print(f"Абсолютная погрешность: {np.abs(2 - res_trap)}")
print(f"Относительная погрешность: {(np.abs(2 - res_trap)) / 2 * 100} %")

# метод Монте-Карло для N
x_plt = np.arange(a, b - h, h)
res_MK = 0
for x in x_plt:
    temp = random.random() * (b - a) + a
    res_MK += (f(temp) + f(temp + h)) / 2 * h
print(f"\nМетодом Монте-Карло для N отрезков: {res_MK}")
print(f"Абсолютная погрешность: {np.abs(2 - res_MK)}")
print(f"Относительная погрешность: {(np.abs(2 - res_MK)) / 2 * 100} %")

# метод Монте-Карло для 100
h_100 = (b - a) / 100
x_plt = np.arange(a, b - h_100, h_100)
res_MK_100 = 0
for x in x_plt:
    temp = random.random() * (b - a) + a
    res_MK_100 += (f(temp) + f(temp + h)) / 2 * h
print(f"\nМетодом Монте-Карло для 100 отрезков: {res_MK_100}")
print(f"Абсолютная погрешность: {np.abs(2 - res_MK_100)}")
print(f"Относительная погрешность: {(np.abs(2 - res_MK_100)) / 2 * 100} %")

# метод Монте-Карло для 10
h_10 = (b - a) / 10
x_plt = np.arange(a, b - h_10, h_10)
res_MK_10 = 0
for x in x_plt:
    temp = random.random() * (b - a) + a
    res_MK_10 += (f(temp) + f(temp + h)) / 2 * h
print(f"\nМетодом Монте-Карло для 10 отрезков: {res_MK_10}")
print(f"Абсолютная погрешность: {np.abs(2 - res_MK_10)}")
print(f"Относительная погрешность: {(np.abs(2 - res_MK_10)) / 2 * 100} %")

# метод Симпсона
temp = 0.0
x = a + h
for i in range(1, int(N / 2 + 1)):
    temp += 4 * f(x)
    x += 2 * h

x = a + 2 * h
for i in range(1, int(N / 2)):
    temp += 2 * f(x)
    x += 2 * h

res_simp = (h / 3) * (f(a) + f(b) + temp)
print(f"\nМетодом Симпсона: {res_simp}")
print(f"Абсолютная погрешность: {np.abs(2 - res_simp)}")
print(f"Относительная погрешность: {(np.abs(2 - res_simp)) / 2 * 100} %")
