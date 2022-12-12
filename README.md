Final Report

Summary:
The program I wrote was to simulate the board game "Othello." Its main features are setting he board size using user input, live score tracking, player turn updates, a win screen, a GUI and user piece placement. The user can input the number of rows they want the game board to be through the terminal, the score is updated upon every turn, and the player's turn is displayed on the top right in red. Additonally, the player who won and their score is displayed on a blank screen, and every piece is placed through a user's click. Finally, the whole game can be done with a visually appealing GUI, which was created through the Arcade module. The only expected applications for this is to play Othello when there is no physical game board present, or, to enhance the players experience of playing the game in general.

Overview: 
There are 2 classes... GameBoard and Othello. Gameboard is the class that draws the board and sets the size using one method called "draw_game". This is called using the "on_draw" function in Othello repeatedly. Othello is the class that deals with running the literal game. It has 11 methods that helps to perform each of the aforementioned features. For example, there's methods to switch who's turn it is, calculate the score, place pieces with a mouse click, and to display who wins the game. No classes inherit from another, and there are no classes that contain objects of other classes in their attributes.

Instructions:
1. Learn how to play Othello
2. Click run to run the program
3. Input how many rows you want the board to be
4. Input player 1 name
5. Input player 2 name
6. Click on the center of a tile to place a piece when its your turn
(Unfortunately I was not able to make the tiles auto flip so work around that)

Future directions:
To develop this program further, someone should add...
1. Auto centering of the pieces, meaning a user could click anywhere within a tile and it would auto center the piece.
2. Improving the auto flip function, which does not work in my program
3. Add a play again option to allow the users to easily play the game again
