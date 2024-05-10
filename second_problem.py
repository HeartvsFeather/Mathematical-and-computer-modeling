import random as r

class Main:
    def game(self):
        # ввод параметров p, x и y
        try:
            p = float(input("Введите вероятность выпадение орла в формате (0.00): "))
            if p > 1. or p < 0.:
                print("\nВероятность может быть только в диапозоне от 0 до 1")
                input("Enter для закрытия")
                return
        except ValueError:
            print("\nНекорректно введена вероятность")
            input("Enter для закрытия")
            return
        try:
            x = int(input("Введите баланс первого (целое число больше 0): "))
            if x < 0:
                print("\nБаланс меньше нуля")
                input("Enter для закрытия")
                return
        except ValueError:
            print("\nНекорректно введен баланс")
            input("Enter для закрытия")
            return
        try:
            y = int(input("Введите баланс второго (целое число больше 0): "))
            if y < 0:
                print("\nБаланс меньше нуля")
                input("Enter для закрытия")
                return
        except ValueError:
            print("\nНекорректно введен баланс")
            input("Enter для закрытия")
            return

        # переменные для расчетов игры с полным разорением
        n = 1000
        n_game = 1000
        fir_w_count = 0
        sec_w_count = 0
        tie_count = 0
        round_count = 0

        # переменные для расчетов игры без полного разорения
        fir_w_count_wfr = 0
        sec_w_count_wfr = 0
        tie_count_wfr = 0

        # расчет игр
        for i in (range(n_game)): # все n_game игр
            balance = 0
            for j in (range(n)): # n раундов в n_game игр
                if r.random() < p: # победа первого с учетом вероятности выпадения орла
                    balance += 1
                else:
                    balance -= 1 # победа второго
                if balance == y: # полное разорение второго
                    fir_w_count += 1
                    fir_w_count_wfr += 1
                    round_count += j + 1
                    break
                if balance == -x: # полное разорение перовго
                    sec_w_count += 1
                    sec_w_count_wfr += 1
                    round_count += j + 1
                    break
            # отдельный подсчет игр без полного разорения
            if balance != -x and balance != y:
                tie_count += 1
                round_count += j + 1
                if balance < (-x + y) / 2:
                    sec_w_count_wfr += 1
                elif balance > (-x + y) / 2:
                    fir_w_count_wfr += 1
                else:
                    tie_count_wfr += 1

        # вывод результатов расчетов
        print(f"\nПобеды первого: {fir_w_count}")
        print(f"Победы второго: {sec_w_count}")
        print(f"Ничьи: {tie_count}")

        # ответы на поставленные вопросы проблемы
        print(f"\nВероятность победы первого: {fir_w_count / n_game}")
        print(f"Вероятность победы второго: {sec_w_count / n_game}")
        print(f"Средняя продолжительность игры: {int(round_count / n)} (раунд) из {n} "
              f"(раунд)")

        # вывод результатов расчетов без полного разорения
        print(f"\nПобеды первого если учесть игру без полного разорения: {fir_w_count_wfr}")
        print(f"Победы второго если учесть игру без полного разорения: {sec_w_count_wfr}")
        print(f"Ничьи если учесть игру без полного разорения: {tie_count_wfr}")

        # ответы на поставленные вопросы проблемы без полного разорения
        print(f"\nВероятность победы первого если учесть игру без полног разорения: {fir_w_count_wfr / n_game}")
        print(f"Вероятность победы второго если учесть игру без полног разорения: {sec_w_count_wfr / n_game}")
        print(f"Средняя продолжительность игры: {int(round_count / n)} (раунд) из {n} (раунд)")

        input("\nEnter для закрытия")
        return


if __name__ == "__main__":
    main = Main()
    main.game()
