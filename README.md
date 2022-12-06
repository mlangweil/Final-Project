Final Report

Summary:
The program I wrote was to simulate the board game "Othello." Its main features are setting he board size using user input, live score tracking, player turn updates, a win screen, a GUI and user piece placement. The only expected applications for this is to play Othello when there is no physical game board present, or, to enhance the players experience of playing the game in general.

Overview: 
There are 2 classes... GameBoard and Othello. Gameboard is the class that draws the board and sets the size using one method called "draw_game". This is called using the "on_draw" function in Othello repeatedly. Othello is the class that deals with running the literal game. It has 11 methods that helps to perform each of the aforementioned features. For example, there's methods to switch who's turn it is, calculate the score, place pieces with a mouse click, and to display who wins the game. No classes inherit from another, and there are no classes that contain objects of other classes in their attributes.
