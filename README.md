# dot-game-solver
python implementation of Dot Game solver

Game is by [@Ouzzgame](https://twitter.com/OuzzGame)


## Implementation of code
1. Cleans the input
* only allows strings of length 4, 9, or 16, and only contains 0,1,2,3,4
2. Format input into MxM square of ints and use that as the data for Matrix class
* all data and functions are now in a Matrix object
3. Matrix class
   
   The Matrix class has two properties, data and answers
   
   data is the grid itelf with the numbers between 0 and 4
   
   answers is the grid where the results will be. answers is a M+1 x M+1 sized 2d array. each data touches 4 answers. the relationship between data and answers have a upper left, upper right, bottom right and bottom left answer. 

1.The upper left answer is the row, col for the data. 
2.The upper right answer is the row+1, col for the data.
3.The bottom right answer is the row+1, col+1 for the data. 
4.The bottom left answer is the row, col+1 for the data.
