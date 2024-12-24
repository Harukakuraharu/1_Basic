import random
from datetime import datetime


class Cell:
    def __init__(self, around_mines: int = 0, mine: bool = False) -> None:
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open: bool = False


class GamePole:
    def __init__(self, N: int, M: int) -> None:
        self.N = N
        self.M = M
        self.pole = [[Cell() for x in range(self.N)] for y in range(self.N)]
        self.opened_cells = 0
        self.safe_cells = self.N * self.N - self.M
        self.init()

    def set_mines(self) -> None:
        """Set mines for pole"""

        mine_position = random.sample(range(self.N * self.N), self.M)
        for mine in mine_position:
            row = mine // self.N
            col = mine % self.N
            self.pole[row][col].mine = True

    def set_around_mines(self) -> None:
        """Set count of the mine on neighbour cells"""
        for row in range(self.N):
            for col in range(self.N):
                if self.pole[row][col].mine:
                    self.calc_around_mines(row, col)

    def calc_around_mines(self, row: int, col: int) -> None:
        """Calculate count of the mine on neighbour cells"""
        for x in range(row - 1, row + 2):
            for y in range(col - 1, col + 2):
                if 0 <= x < self.N and 0 <= y < self.N:
                    self.pole[x][y].around_mines += 1

    def init(self) -> None:
        """Initial game board"""

        self.set_mines()
        self.set_around_mines()

    def show(self) -> None:
        """Show board on console"""

        for i in range(self.N):
            rows = []
            for j in range(self.N):
                if not self.pole[i][j].fl_open:
                    rows.append("# ")
                elif self.pole[i][j].mine:
                    rows.append("* ")
                else:
                    rows.append(f"{(self.pole[i][j].around_mines)} ")
            print(*rows)


class Game:
    def __init__(self, pole=10, mine=12):
        # pole = int(input("Введите размер поля: "))
        # mine = int(input("Введите количество бомб: "))
        self.pole = pole
        self.mine = mine
        self.game = GamePole(self.pole, self.mine)

    def check_win(self) -> bool:
        """Check user for win"""
        return self.game.opened_cells == self.game.safe_cells

    def choose_cell(self) -> None:
        """Choose cell for playing game"""

        start_time = datetime.now()
        flag = True
        while flag:
            self.game.show()
            row, col = map(
                int,
                input("Введите координаты клетки (строка, столбец): ").split(),
            )
            row -= 1
            col -= 1
            if self.game.pole[row][col].mine:
                self.game.pole[row][col].fl_open = True
                self.game.show()
                print("Упс! Бомба взорвалась")
                print(f"Время игры: {datetime.now() - start_time}")
                flag = False
            else:
                self.next_step(row, col)
                if self.check_win():
                    self.game.show()
                    print("Поздравляем! Вы выиграли!")
                    print(f"Время игры: {datetime.now() - start_time}")
                    flag = False

    def next_step(self, row: int, col: int) -> None:
        """Play game if not find mine"""

        self.game.pole[row][col].fl_open = True
        self.game.opened_cells += 1
        if self.game.pole[row][col].around_mines == 0:
            for i in range(row - 1, row + 2):
                if 0 <= i < self.game.N and not self.game.pole[i][col].fl_open:
                    self.next_step(i, col)
            for j in range(col - 1, col + 2):
                if 0 <= j < self.game.N and not self.game.pole[row][j].fl_open:
                    self.next_step(row, j)


# if __name__ == "__main__":
#     game_1 = Game()
#     game_1.choose_cell()
