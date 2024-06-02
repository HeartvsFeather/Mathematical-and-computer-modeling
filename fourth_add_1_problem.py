import numpy as np

class Main:
    def chord_method(self):
        def f(x): # возвращает значения f(x)
            return -np.sin(x) * np.e ** x ** 2 + x / np.cos(x)

        # изначальные данные для метода хорд
        pre_res = 3.1414300026834985 # аналитическое решение
        a = 3 # начало отрезка
        b = 3.2 # конец отрезка
        eps = 1e-5 # точность

        # проверка на факт пересечения функции оси OX
        if f(a) * f (b) > 0:
            print("Функция f(x) на [a;b] не пересекает x = 0. Решения нет")

        while (True):
            # выведено из двух уравнений прямых по двум точкам
            c = a - (((b - a) * f(a)) / (f(b) - f(a)))
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
            if abs(b - a) < eps:
                break
        res = c

        # ответы на поставленные вопросы
        print(f"\nФункция f(x) на [a;b] пересекает OX в точке: {'{:.6f}'.format(res)}")
        print(f"Абсолютная погрешность: {'{:.6f}'.format(abs(res - pre_res))}")
        print(f"Относительная погрешность: {abs(res - pre_res) / pre_res * 100} %")

        input("\nEnter для закрытия")
        return


if __name__ == "__main__":
    main = Main()
    main.chord_method()
