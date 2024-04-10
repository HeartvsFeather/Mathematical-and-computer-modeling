import random as r

class Main:
    def game(self):
        # enter p, x, y
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

        # variables for future count
        n = 1000
        n_game = 1000
        fir_w_count = 0
        sec_w_count = 0
        tie_count = 0
        round_count = 0

        # variables for future count without full ruin
        fir_w_count_wfr = 0
        sec_w_count_wfr = 0
        tie_count_wfr = 0

        # calculation of game
        for i in (range(n_game)): # games
            balance = 0
            for j in (range(n)): # rounds in one game
                if r.random() < p:
                    balance += 1
                else:
                    balance -= 1
                if balance == y:
                    fir_w_count += 1
                    fir_w_count_wfr += 1
                    round_count += j + 1
                    break
                if balance == -x:
                    sec_w_count += 1
                    sec_w_count_wfr += 1
                    round_count += j + 1
                    break
            if balance != -x and balance != y: # additional calc for no total ruin
                tie_count += 1
                round_count += j + 1
                if balance < (-x + y) / 2:
                    sec_w_count_wfr += 1
                elif balance > (-x + y) / 2:
                    fir_w_count_wfr += 1
                else:
                    tie_count_wfr += 1

        # results
        print(f"\nПобеды первого: {fir_w_count}")
        print(f"Победы второго: {sec_w_count}")
        print(f"Ничьи: {tie_count}")

        # answer to questions of problem
        print(f"\nВероятность победы первого: {fir_w_count / n_game}")
        print(f"Вероятность победы второго: {sec_w_count / n_game}")
        print(f"Средняя продолжительность игры: {int(round_count / n)} (раунд) из {n} (раунд)")

        # results of game without total ruin
        print(f"\nПобеды первого если учесть игру без полного разорения: {fir_w_count_wfr}")
        print(f"Победы второго если учесть игру без полного разорения: {sec_w_count_wfr}")
        print(f"Ничьи если учесть игру без полного разорения: {tie_count_wfr}")

        # answer to questions of problem without total ruin
        print(f"\nВероятность победы первого если учесть игру без полног разорения: {fir_w_count_wfr / n_game}")
        print(f"Вероятность победы второго если учесть игру без полног разорения: {sec_w_count_wfr / n_game}")
        print(f"Средняя продолжительность игры: {int(round_count / n)} (раунд) из {n} (раунд)")

        input("\nEnter для закрытия")
        return


if __name__ == "__main__":
    main = Main()
    main.game()
