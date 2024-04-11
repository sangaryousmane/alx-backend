#!/usr/bin/env python3
""" Implement nqueens using Recursion X Backtracking
"""
import sys


import sys

class NQueen:
    def __init__(self, n):
        self.n = n
        self.board = [[False for _ in range(self.n)] for _ in range(self.n)]
        self.solutions = []

    def main(self):
        self.queens(self.board, 0)
        self.display_solutions()

    def queens(self, board, row):
        if row == len(board):
           self.solutions.append(self.get_queen_positions(board))
           return

        for col in range(len(board)):
            if self.isSafe(board, row, col):
                board[row][col] = True
                self.queens(board, row + 1)
                board[row][col] = False

    def isSafe(self, board, row, col):
        for i in range(row):
            if board[i][col]:
                return False

        for i in range(1, min(row, col) + 1):
            if board[row - i][col - i]:
                return False

        for i in range(1, min(row, self.n - col - 1) + 1):
            if board[row - i][col + i]:
                return False

        return True

    def get_queen_positions(self, board):
        positions = []
        for row in range(self.n):
            for col in range(self.n):
                if board[row][col]:
                    positions.append([row, col])
        return positions

    def display_solutions(self):
        for solution in self.solutions:
              print(solution)

def print_usage_error_and_exit(message):
    print(message)
    sys.exit(1)

def Main(input):
  try:
      N = int(input)
      if N < 4:
        print_usage_error_and_exit('N must be at least 4')
      n_queen = NQueen(N)
      n_queen.main()
  except ValueError:
      print_usage_error_and_exit('N must be a number')

if __name__ == '__main__':
  if len(sys.argv) != 2:
      print_usage_error_and_exit('Usage: ./0-nqueens.py N')

  Main(sys.argv[1])

