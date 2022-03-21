class Test:
    def __init__(self, limit):
        self.x = 10
        self.y = 10
        self.grid = [[x for x in range(10)] for y in range(10)]
        self.iter_x = 0
        self.iter_y = 0

    def __iter__(self):
        return self

    def __next__(self):
        curr_x = self.iter_x
        curr_y = self.iter_y
        if curr_x == self.x:
            curr_y += 1
            curr_x = 0

        if curr_y == self.y:
            curr_y = 0
            curr_x = 0
            raise StopIteration
     
        self.iter_x = curr_x + 1
        self.iter_y = curr_y
        return self.grid[curr_x][self.iter_y]

    def print_grid(self):
        for y in range(self.y):
            for x in range(self.x):
                print(self.grid[x][y], end=" | ")
            print("")


def main():
    for i in Test(100):
        print(i)

main()
