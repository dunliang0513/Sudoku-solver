# Sudoku solver using Backtracking Algorithm




![Sudoku Solver Demo](sudoku_solver_demo.gif)

This Python project implements a Sudoku solver using the backtracking algorithm. Given an incomplete Sudoku puzzle, the solver aims to fill in all the missing numbers while adhering to the Sudoku rules.


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [How it Works](#how-it-works)

## Introduction

Sudoku is a popular logic-based number puzzle where you need to fill a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 subgrids contain all of the digits from 1 to 9 without repetition. This project provides a Python solution to automatically solve Sudoku puzzles using the backtracking algorithm.

## Features

- Sudoku puzzle solver using backtracking algorithm.
- Input Sudoku puzzles in a simple text format.
- Clear visualization of the solved Sudoku grid.

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/dunliang0513/sudoku-solver.git
   cd sudoku-solver
   ```

2. Edit the `puzzle` inside the `main.py`:


   Input the sudoku that you want to solve.

3. The solver will display the solved Sudoku grid in the console.

<img width="188" alt="Screenshot 2023-09-17 at 4 23 48 PM" src="https://github.com/dunliang0513/Sudoku-solver/assets/81207108/4e4f15cb-0102-4a54-a7aa-b85f153b5999">


## How it Works

The Sudoku solver is implemented using the backtracking algorithm. It works as follows:

1. Find an empty cell in the Sudoku grid.
2. Try filling the cell with a number from 1 to 9.
3. Check if the number is valid in that position (no conflicts with the current row, column, or 3x3 subgrid).
4. If the number is valid, move to the next empty cell and repeat the process.
5. If no valid number can be placed, backtrack to the previous cell and try a different number.
6. Continue this process until the entire grid is filled.

The algorithm guarantees a solution if one exists, and it backtracks when it encounters conflicts.
