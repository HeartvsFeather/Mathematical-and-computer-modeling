import numpy as np

class Main:
    def fixed_point_iteration(self):
        def f(x): # возвращает значения f(x)
            return np.sin(x) * np.log10(x + 1) - x + 3

        def g(x): # возвращает значения x = g(x), выведенного из f(x)
            return np.sin(x) * np.log10(x + 1) + 3

        # изначальные данные для метода простых итерация
        x0 = 0.3 # начальное предположение корня
        pre_res = 3.05348505386190 # аналитическое решение
        eps = 1e-5 # точность
        step = 1
        conver = 1
        flag = True

        while flag:
            x1 = g(x0)
            x0 = x1
            step += 1
            # проверка на количество шагов, чтобы проверить не сходимость
            if step > 1000:
                conver=0
                break
            flag = abs(f(x1)) > eps # проверка на требуемую точность
        res = x1

        # ответы на поставленные вопросы
        if conver == 1:
            print(f"\nФункция f(x) на пересекает OX в точке: {'{:.6f}'.format(res)}")
            print(f"Абсолютная погрешность: {'{:.6f}'.format(abs(res - pre_res))}")
            print(f"Относительная погрешность: {abs(res - pre_res) / pre_res * 100} %")
        else:
            print("\nМетод не сходится")

        input("\nEnter для закрытия")
        return


if __name__ == "__main__":
    main = Main()
    main.fixed_point_iteration()
