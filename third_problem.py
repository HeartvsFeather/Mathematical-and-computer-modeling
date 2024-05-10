import numpy as np
import random

class Main:
    def calc_of_integral(self):
        def f(x): # возвращает значения f(x)
            return np.sqrt((1 - np.cos(2 * x)) / 2) # первый вариант
            # return (x + np.cos(x)) / (np.square(x) + 2 * np.sin(x)) # второй вариант\
            # return np.sin(x ** 2) # неберущийся интеграл

        # первый вариант
        a = 0
        b = np.pi
        # второй вариант
        # a = 1
        # b = np.sqrt(3)

        # переменные для последующих вычеслений
        N = 1000 # количество прямоугольников
        h = (b - a) / N # ширина прямоугольника

        print(f"\nАналитическое решение: 2") # для первого варианта

        # вычисления площадей под функцией f(x) на отрезке от a до b включительно
        # метод левых прямоугольников
        x_plt = np.arange(a, b - h, h)
        res_left = 0
        for x in x_plt:
            res_left += f(x) * h
        print(f"\nМетодом левых прямоугольников: {res_left}")
        print(f"Абсолютная погрешность: {np.abs(2 - res_left)}")
        print(f"Относительная погрешность: {(np.abs(2 - res_left)) / 2 * 100} %")

        # метод правых прямогульников
        x_plt = np.arange(a + h, b, h)
        res_right = 0
        for x in x_plt:
            res_right += f(x) * h
        print(f"\nМетодом правых прямоугольников: {res_right}")
        print(f"Абсолютная погрешность: {np.abs(2 - res_right)}")
        print(f"Относительная погрешность: {(np.abs(2 - res_right)) / 2 * 100} %")

        # метод трапеций
        x_plt = np.arange(a, b - h, h) # можно взять и правые, суть не меняется
        res_trap = 0
        for x in x_plt:
            res_trap += (f(x) + f(x + h)) / 2 * h
        print(f"\nМетодом трапеций: {res_trap}")
        print(f"Абсолютная погрешность: {np.abs(2 - res_trap)}")
        print(f"Относительная погрешность: {(np.abs(2 - res_trap)) / 2 * 100} %")

        # метод Монте-Карло для N
        x_plt = np.arange(a, b - h, h) # можно взять и правые, суть не меняется
        res_MK = 0
        for x in x_plt:
            temp = random.random() * (b - a) + a # выбираем на отрезке [a,b]
            res_MK += (f(temp) + f(temp + h)) / 2 * h
        print(f"\nМетодом Монте-Карло для {N} отрезков: {res_MK}")
        print(f"Абсолютная погрешность: {np.abs(2 - res_MK)}")
        print(f"Относительная погрешность: {(np.abs(2 - res_MK)) / 2 * 100} %")

        # метод Монте-Карло для 500
        h_500 = (b - a) / 500
        x_plt = np.arange(a, b - h_500, h_500)
        res_MK_500 = 0
        for x in x_plt:
            temp = random.random() * (b - a) + a
            res_MK_500 += (f(temp) + f(temp + h)) / 2 * h
        print(f"\nМетодом Монте-Карло для 500 отрезков: {res_MK_500}")
        print(f"Абсолютная погрешность: {np.abs(2 - res_MK_500)}")
        print(f"Относительная погрешность: {(np.abs(2 - res_MK_500)) / 2 * 100} %")

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
        # для нечетных
        x = a + h
        for i in range(1, int(N / 2 + 1)):
            temp += 4 * f(x)
            x += 2 * h

        # для четных
        x = a + 2 * h
        for i in range(1, int(N / 2)):
            temp += 2 * f(x)
            x += 2 * h

        res_simp = (h / 3) * (f(a) + f(b) + temp)
        print(f"\nМетодом Симпсона: {res_simp}")
        print(f"Абсолютная погрешность: {np.abs(2 - res_simp)}")
        print(f"Относительная погрешность: {(np.abs(2 - res_simp)) / 2 * 100} %")

        input("\nEnter для закрытия")
        return


if __name__ == "__main__":
    main = Main()
    main.calc_of_integral()
