class EightQueens:
    def __init__(self, size):
        self.size = size
        self.solutions = 0
        self.Start()

    def Start(self):
        positions = [-1] * self.size
        self.PlaceQueen(positions, 0)
        print("Se han encontrado: " + str(self.solutions) + " soluciones.")

    def PlaceQueen(self, positions, row):
        if row == self.size:
            self.PrintSolution(positions)
            self.solutions += 1
        else:
            for column in range(self.size):
                if self.ValidatePlace(positions, row, column):
                    positions[row] = column
                    self.PlaceQueen(positions, row + 1)

    def ValidatePlace(self, positions, rows, column):
        for i in range(rows):
            if positions[i] == column or \
                    positions[i] - i == column - rows or \
                    positions[i] + i == column + rows:

                return False
        return True

    def PrintSolution(self, positions):
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "R "
                else:
                    line += ". "
            print(line)
        print("\n")


def Main():
    EightQueens(8)


Main()
