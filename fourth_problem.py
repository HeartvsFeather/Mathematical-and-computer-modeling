import numpy as np

class Main:
    def bisection_method(self):
        def f(x): # возвращает значения f(x)
            return np.sin(x) * np.e ** x ** 2 + x / np.cos(x)

        # получение знака функции при аргументе равном x
        def getSign(x):
            if x >= 0:
                return 1
            else:
                return 0

        x_a = 3 # левая координата отрезка
        x_b = 3.2 # правая координата отрезка
        eps = 1e-12 # требуемая точность

        n_count_first = 0 # счетчик для первого нахождения
        n_count_second = 0 # счетчик для второго нахождения

        # нахождение корня
        while x_b - x_a > eps: # требуемая точность при проверки длины от x_a до x_b
            dx = (x_b - x_a) / 2
            x_i = x_a + dx
            if getSign(f(x_a)) != getSign(f(x_i)):
                x_b = x_i
            else:
                x_a = x_i
            n_count_first += 1
        res_1 = x_i

        # нахождение корня, но требуемая точность
        # при проверки длины от x_i текущего и x_i прошедшего (x_i_past)
        x_a = 3
        x_b = 3.2
        x_i_past = 0
        while True:
            dx = (x_b - x_a) / 2
            x_i = x_a + dx
            if abs(x_i_past - x_i) < eps:
                break
            if getSign(f(x_a)) != getSign(f(x_i)):
                x_b = x_i
            else:
                x_a = x_i
            x_i_past = x_i
            n_count_second += 1
        res_2 = x_i

        print(f"\nКорень уравнения: {'{:.5f}'.format(res_1)} при {n_count_first} итераций"
              f" и проверки требуемой точности от левого смещения до правого смещения")
        print(f"\nКорень уравнения: {'{:.5f}'.format(res_2)} при {n_count_second} "
              f"итераций и проверки требуемой точности от прошлого итерируемого центра "
              f"отрезка до нового")

        input("\nEnter для закрытия")
        return


if __name__ == "__main__":
    main = Main()
    main.bisection_method()
