import numpy as np
import matplotlib.pyplot as plot

class Main:
    def gradient_descent(self):
        # ввод начального положения
        try:
            x_null = float(input("Введите начальную точку в формате 0.00 от -5 до 5: "))
            if x_null < -5.0 or x_null > 5.0:
                print("\nНачальное положение может быть только в диапозоне от -5 до 5")
                input("Enter для закрытия")
                return
        except ValueError:
            print("\nНекорректно введено начальное положение")
            input("Enter для закрытия")
            return

        def f(x): # возвращает значения f(x)
            return np.cos(3 * x) + 0.2 * x

        def df(x): # возвращает значения f'(x)
            return -3 * np.sin(3 * x) + 0.2

        # значения x и f(x) с шагом 0.01 (*определяет точность решения) от -5 до 5
        x_plt = np.arange(-5.0, 5.0, 0.01) # x
        f_plt = [f(x) for x in x_plt] # f(x)

        N = 1000 # количество шагов
        lr = 0.01 # длина шага смещения

        # параметры для отображения графика
        fig, ax = plot.subplots()
        ax.grid(True)
        ax.plot(x_plt, f_plt) # f(x) на графике

        # проверка на изначальное попадание в экстремум
        if df(x_null) == 0:
            x -= 0.01
        else:
            x = x_null

        # вычисление x и f(x) после спуска по принципу x = x - f'(x)
        for i in range(N):
            # перменные для отображения стрелок
            x_prev = x
            y_prev = f(x)

            x = x - lr * np.sign(df(x)) # шаг с длиной lr вправо или влево в зависимости
                                        # от знака производной

            # добавление стрелки на график
            if x_prev >= x:
                dx = -(x_prev - x)
            else:
                dx = x - x_prev
            if y_prev >= f(x):
                dy = -(y_prev - f(x))
            else:
                dy = f(x) - y_prev
            plot.arrow(x = x_prev, y = y_prev, dx = dx, dy = dy, width= 0.02)

            # проверка на зацикленность возле точки минимума
            if np.sign(df(x)) != np.sign(df(x_prev)):
                    break

        # вывод полученного результата
        print(f"\nГрадиентный спуск нас привел от точки с координатами "
              f"({'{:.2f}'.format(x_null)}, {'{:.2f}'.format(f(x_null))}) к точке c "
              f"координатами ({'{:.2f}'.format(x)}, {'{:.2f}'.format(f(x))}) на "
              f"функции cos(3x) + 0.2x (погрешность +- 0.01)")

        plot.show() # отображение графика

        input("\nEnter для закрытия")
        return


if __name__ == "__main__":
    main = Main()
    main.gradient_descent()
