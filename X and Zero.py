map = [1, 2, 3,        # Инициализация карты
        4, 5, 6,
        7, 8, 9]

wins = [[0, 1, 2],      # Инициализация победных линий
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


def print_map():          # Вывод карты на экран
    print(map[0], end=" ")
    print(map[1], end=" ")
    print(map[2])

    print(map[3], end=" ")
    print(map[4], end=" ")
    print(map[5])

    print(map[6], end=" ")
    print(map[7], end=" ")
    print(map[8])

print("Понеслась!!!")

def step_map(step, symbol):     # Сделать ход в ячейку
    ind = map.index(step)
    map[ind] = symbol

def get_result():              # Получить текущий результат игры
    win = ""

    for i in wins:
        if map[i[0]] == "X" and map[i[1]] == "X" and map[i[2]] == "X":
            win = "X"
        if map[i[0]] == "O" and map[i[1]] == "O" and map[i[2]] == "O":
            win = "O"

    return win



game_over = False            # Основная программа
player1 = True

while game_over == False:

    # 1. Показываем карту
    print_map()

    # 2. Спросим у играющего куда делать ход
    if player1 == True:
        symbol = "X"
        step = int(input("Ходит Х: "))
    else:
        symbol = "O"
        step = int(input("Ходит 0: "))

    step_map(step, symbol)  # делаем ход в указанную ячейку
    win = get_result()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

# Игра окончена. Покажем карту. Объявим победителя.
print_map()
print(f"Победитель {win} !!!!")