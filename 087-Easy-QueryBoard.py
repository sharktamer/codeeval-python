#!/usr/bin/python

import sys

board = [[0] * 256] * 256


def setRow(i, x):
    global board
    board[int(i)] = [x] * 256


def setCol(j, x):
    global board
    tempBoard = list(zip(*board))
    tempBoard[int(j)] = [x] * 256
    board = list(zip(*tempBoard))


def queryRow(i):
    print(sum([int(x) for x in board[int(i)]]))


def queryCol(j):
    print(sum([int(x) for x in list(zip(*board))[int(j)]]))

funDict = {'SetRow': setRow, 'SetCol': setCol,
           'QueryRow': queryRow, 'QueryCol': queryCol}

with open(sys.argv[1]) as f:
    for line in f:
        f = funDict[line.strip().split()[0]]
        args = line.split()[1:]
        f(*args)
