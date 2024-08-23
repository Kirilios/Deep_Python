'''
Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга
 и check_queens(queens),
которая проверяет все возможные пары ферзей.
Известно, что на доске 8×8 можно расставить 8 ферзей так,
чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите,
есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел,
каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
 Не забудьте напечатать результат.
'''

queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]

def is_attacking(q1,q2):
    row1, col1 = q1
    row2, col2 = q2
    same_diag = abs(row1 - row2) == abs(col1 - col2)
    if row1 == row2 or col1 == col2 or same_diag:
        return True
    return False

def check_queens(queens):
    desk_size = len(queens)
    for i in range(desk_size):
        for j in range(i + 1, desk_size):
            if is_attacking(queens[i], queens[j]):
                return True
    return False

if __name__ == '__main__':
    res = check_queens(queens)
    print(res)

#2

