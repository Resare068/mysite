import time
from random import randrange
from copy import deepcopy

class Life:
    def __init__(self):
        self.height = 18
        self.width = 48
        self.judge = 0
        self.cnt = 0
        self.field = [[randrange(2) for i in range(self.width)] for j in range(self.height)]
        self.nfield = [[0 for i in range(self.width)] for j in range(self.height)]
        self.lfield = [[0 for i in range(self.width)] for j in range(self.height)]
        self.llfield = [[0 for i in range(self.width)] for j in range(self.height)]

    def display_field(self):
        self.judge = 0
        for i in range(self.height):
            for j in range(self.width):
                output = " "
                output = "@" if self.field[i][j] == 1 else output
                print(output, end="")
                life = 0
                life = 1 if self.counter(i, j) == 3 else life
                life = self.field[i][j] if self.counter(i, j) == 2 else life
                self.nfield[i][j] = life
            print()
            if not 1 in self.nfield[i]:
                self.judge += 1
        self.llfield = deepcopy(self.lfield)
        self.lifeld = deepcopy(self.field)
        self.field = deepcopy(self.nfield)

    def counter(self, y, x):
        cnt = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if self.field[(y + i) % self.height][(x + j) % self.width] == 1:
                    cnt += 1
        return cnt

    def play(self):
        for i in range(100):
            self.display_field()
            print("-" * self.width)
            time.sleep(0.2)

    def play_to_end(self):
        while True:
            self.display_field()
            self.cnt += 1
            print("=" * self.width)
            if self.judge == self.height or self.llfield == self.field:
                print("count :", self.cnt)
                break
            time.sleep(0.2)

if __name__ == "__main__":
    l = Life()
    l.play_to_end()
