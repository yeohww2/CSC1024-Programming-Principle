# Tic-Tac-Toe Game

## Overview

Welcome to the **Tic-Tac-Toe Game**! This is a simple implementation of the classic Tic-Tac-Toe game where a human player competes against a computer player. The player who manages to align three of their symbols (either 'X' or 'O') horizontally, vertically, or diagonally wins the game.

The computer player is programmed to make smart moves and can block or win based on the current state of the game.

## Game Features

- **Player vs Computer:** You can play against the computer which uses basic logic to make its moves.
- **Automatic move validation:** The game checks for valid moves and ensures that players can only select free spaces.
- **Randomized player start:** The game randomly selects who goes first, the player or the computer.
- **Win/Lose conditions:** The game determines the winner when three matching symbols are aligned, or declares a draw when no moves are left.

## Instructions

1. The player can choose to play as 'X' or 'O'.
2. Players take turns placing their mark on the board.
3. To make a move, the player must input a number (1-9), corresponding to a position on the board.
4. The game will end when:
   - A player wins by forming a straight line of three of their symbols.
   - The board is full and there is no winner, resulting in a draw.
