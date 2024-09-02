'''
Создайте программу, которая реализует игру «Крестики-нолики».
Для этого напишите:
1. Класс, который будет описывать поле игры.
class Board:
# Класс поля, который создаёт у себя экземпляры клетки.
# Пусть класс хранит информацию о состоянии поля (это может быть список из
девяти элементов).
# Помимо этого, класс должен содержать методы:
# «Изменить состояние клетки». Метод получает номер клетки и, если клетка не
занята, меняет её состояние. Если состояние удалось изменить, метод возвращает
True, иначе возвращается False.
# «Проверить окончание игры». Метод не получает входящих данных, но
возвращает True/False. True — если один из игроков победил, False — если
победителя нет.
2. Класс, который будет описывать одну клетку поля:
class Cell:
# Клетка, у которой есть значения:
# занята она или нет;
# номер клетки;
# символ, который клетка хранит (пустая, крестик, нолик).
3. Класс, который описывает поведение игрока:
class Player:
# У игрока может быть:
# имя,
# количество побед.
# Класс должен содержать метод:
# «Сделать ход». Метод ничего не принимает и возвращает ход игрока (номер
клетки). Введённый номер нужно обязательно проверить.
4. Класс, который управляет ходом игры:
class Game:
# класс «Игры» содержит атрибуты:
# состояние игры,
# игроки,
# поле.
# А также методы:
# Метод запуска одного хода игры. Получает одного из игроков, запрашивает у
игрока номер клетки, изменяет поле, проверяет, выиграл ли игрок. Если игрок победил,
возвращает True, иначе False.
# Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который
завершается победой одного из игроков или ничьей. Если игра завершена, метод
возвращает True, иначе False.
# Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой
игры, хотят ли игроки продолжать играть. После каждой игры выводится текущий счёт
игроков.
'''

class Cell:
    def __init__(self, number, occupied_state=False, symbol=None):
        self.number = number
        self.occupied_state = occupied_state
        self.symbol = " " #Symbol of cell ('X', '0', or space)

class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def display_board(self):
        print("---------------")
        for i in range(0, 9, 3):
            print(f"| {self.cells[i].symbol} | {self.cells[i+1].symbol} | {self.cells[i+2].symbol} |")
            print("---------------")

    def change_cell(self, cell_number, symbol):
        cell = self.cells[cell_number - 1]
        if cell.occupied_state:
            return False
        cell.symbol = symbol
        cell.occupied_state = True
        return True

    def check_game_over(self):
        win_position = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

        for position in win_position:
            if self.cells[position[0]].symbol != " " and self.cells[position[0]].symbol == self.cells[position[1]].symbol == self.cells[position[2]].symbol:
                return True
            return False

    def reset_board(self):
        for cell in self.cells:
            cell.symbol = " "
            cell.occupied_state = False

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0

    def make_move(self):
        while True:
            try:
                move = int(input(f"{self.name}, enter your move (1-9): "))
                if 1 <= move <= 9:
                    return move
                else:
                    print("Invalid move. Please enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a number.")

class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]

    def launch_move(self, player):
        while True:
            self.board.display_board()
            cell_number = player.make_move()
            if self.board.change_cell(cell_number, player.symbol):
                if self.board.check_game_over():
                    return True
                return False
            print('Cell is occupied. Make another move')

    def play_one_game(self):
        print("Starting game")
        while True:
            for player in self.players:
                if self.launch_move(player):
                    self.board.display_board()
                    print(f"{player.name} wins!")
                    player.wins += 1
                    return
            if all(cell.occupied_state for cell in self.board.cells):
                self.board.display_board()
                print("It's a tie!")
                return

    def start_games(self):
        print('Welcome to tic-n-toes')
        while True:
            self.board.reset_board()
            self.play_one_game()
            print(f"Current score: {self.players[0].name}: {self.players[0].wins}, {self.players[1].name}: {self.players[1].wins}")
            again = input("do you want to continue? (yes/no): ")
            if again.lower()!= "yes":
                print("Goodbye!")
                break

if __name__ == '__main__':
    player1 = Player("Player 1", "X")
    player2 = Player("Player 2", "0")
    game = Game(player1, player2)
    game.start_games()
