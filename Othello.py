import arcade
import numpy as np

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Othello"
SCALING = 2.0
    

class Game_Board():
    def __init__(self, color, rows):
        self.color = color
        self.rows = rows
       

       
    def draw_game_board(self):
        """Draws the game board

        Input: Self
        Output: Drawing
        """
        arcade.draw_rectangle_filled(SCREEN_HEIGHT/2, SCREEN_HEIGHT/2, SCREEN_HEIGHT, SCREEN_HEIGHT, self.color)
        arcade.draw_line(2, 00, 2, SCREEN_HEIGHT, arcade.color.BLACK, 3)
        arcade.draw_line(SCREEN_HEIGHT, 00, SCREEN_HEIGHT, SCREEN_HEIGHT, arcade.color.BLACK, 3)
        arcade.draw_line(0, 1, SCREEN_HEIGHT+1, 1, arcade.color.BLACK, 3)
        arcade.draw_line(0, SCREEN_HEIGHT-1, SCREEN_WIDTH-1, SCREEN_HEIGHT-1, arcade.color.BLACK, 3)
        for distance in range(0, SCREEN_HEIGHT, SCREEN_HEIGHT//self.rows):
                arcade.draw_line(distance, 00, distance, SCREEN_HEIGHT, arcade.color.BLACK, 3)
                arcade.draw_line(0, distance, SCREEN_HEIGHT, distance, arcade.color.BLACK, 3)
     



              
class Othello(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.WHITE) 
        self.othello_piece_list = None
        self.black_piece = None
        self.white_piece = None
        self.MOVE_DIRS = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1), (1, 0), (+1, 1)]
        self.player_2_score = 0
        self.player_1_score = 0
        self.player_turn = ""
      
        self.square_dist = SCREEN_HEIGHT//rows
        self.board_array = np.zeros(shape=(rows, rows), dtype=int)
        self.y = 0
        self.x = 0
        self.change_piece = False
        self.i = 0
        self.row = 0
        self.col = 0
     
    def calculate_score(self):
        """Calculates each players score
        Input: Self
        Output: Integer
        """
        self.player_1_score = np.count_nonzero(self.board_array == 1)
        self.player_2_score = np.count_nonzero(self.board_array == 2)
    
    
        
    def setup(self):
        self.scene = arcade.Scene()
        self.othello_piece_list = arcade.SpriteList() 
        self.black_piece = arcade.Sprite(":resources:onscreen_controls/shaded_dark/unchecked.png", piece_size/25)
        self.white_piece = arcade.Sprite(":resources:onscreen_controls/shaded_light/unchecked.png", piece_size/25)
        self.player_turn = player_1

    def player_turn_display(self):
        """Displays whose turn it is as a drawing
        
        Input: Self
        Output: Integer
        """
        arcade.draw_text(str(self.player_turn) + "'s turn!", 720, 620, arcade.color.RED, 30)


    def show_score(self):
        """Displays the score as a drawing
        
        Input: Self
        Output: Drawing
        """
        self.calculate_score()
        self.player_turn_display()
        arcade.draw_text(str(player_1) + "'s score:\n", 720, 320, arcade.color.BLACK, 30)
        arcade.draw_text(str(self.player_1_score), 780,280, arcade.color.BLACK, 30)
        arcade.draw_text(str(player_2) + "'s score:\n", 720, 220, arcade.color.BLACK, 30)
        arcade.draw_text(str(self.player_2_score), 780,180, arcade.color.BLACK, 30)



    def next_turn(self):
        """ Updates who's turn it is
        
        Input: Self
        Output: String
        """
        if self.player_turn == player_1:
            self.player_turn = player_2
        elif self.player_turn == player_2:
            self.player_turn = player_1



    def flip_pieces(self):
        """Auto flips the pieces on the game board

        Input: Self
        Output: Matrix
        """
        if self.player_turn == player_1:
            for direction in self.MOVE_DIRS:
                while self.change_piece == True or (self.i == rows - self.row) or (self.i == rows - self.col):
                    self.row = self.start_row + (direction[0] * self.i)
                    self.col = self.start_column + (direction[1] * self.i)
                    self.i+=1
                    print(self.row)
                if self.board_array[self.row,self.col] == 2:
                    self.board_array[self.row,self.col] == 1
                else: 
                    break
        if self.player_turn == player_2:
            for direction in self.MOVE_DIRS:
                while self.change_piece == True or (self.i == rows - self.row) or (self.i == rows - self.col):
                    self.row = self.start_row + (direction[0] * self.i)
                    self.col = self.start_column + (direction[1] * self.i)
                    self.i+=1
                    print(self.row)
                if self.board_array[self.row,self.col] == 1:
                    self.board_array[self.row,self.col] == 2
                else: 
                    self.change_piece = False
                
                
    def check_winner(self):
        """Draws who the winner is and presents a win screen
        
        Input: Self
        Output: Drawing
        """
        if self.player_1_score + self.player_2_score == (rows * rows):
            arcade.draw_rectangle_filled(SCREEN_HEIGHT/2, SCREEN_HEIGHT/2, SCREEN_WIDTH*2, SCREEN_WIDTH*2, arcade.color.WHITE)
            if self.player_2_score > self.player_1_score:
                arcade.draw_text(str(player_2) + " wins with a score of " + str(self.player_2_score)+"!", SCREEN_HEIGHT/2, SCREEN_HEIGHT/2, arcade.color.BLACK, 30)
            elif self.player_1_score > self.player_2_score:
                arcade.draw_text(str(player_1) + " wins with a score of " + str(self.player_1_score)+"!", SCREEN_HEIGHT/2, SCREEN_HEIGHT/2, arcade.color.BLACK, 30)
            else:
                arcade.draw_text("It's a tie!", SCREEN_HEIGHT/2, SCREEN_HEIGHT/2, arcade.color.BLACK, 30)

    def player_1_turn(self):
        """Sets the current turn as player 1's
        
        Input: Self
        Output: String
        """
        self.player_turn = player_1

    def player_2_turn(self):
        """Sets the current turn as player 2's
        
        Input: Self
        Output: String
        
        """
        self.player_turn = player_2


    def on_mouse_press(self, x, y, button, modifiers):
        """Places a piece on the board using a user click
        
        Input: Self, Float, Float
        Output: Drawing, List
        """
        self.black_piece = arcade.Sprite(":resources:onscreen_controls/shaded_dark/unchecked.png", piece_size/25)
        self.white_piece = arcade.Sprite(":resources:onscreen_controls/shaded_light/unchecked.png", piece_size/25)

        if self.player_turn == player_1:
            self.current_piece = self.black_piece
        else:
            self.current_piece = self.white_piece
        self.current_piece.center_x = x
        self.current_piece.center_y = y
        self.othello_piece_list.append(self.current_piece)
        self.place_piece()
        self.flip_pieces()
        
        
    def place_piece(self):
        """Places the users piece in a matrix

        Input: Self
        Output: Matrix
        """
        for i in range(0,SCREEN_HEIGHT, self.square_dist):
            if i< self.current_piece.center_x < self.square_dist + i: 
                break
            else: 
                self.x +=1
        for i in range(0,SCREEN_HEIGHT, self.square_dist):
            if i< self.current_piece.center_y < self.square_dist + i:
                break
            else:
                self.y +=1
        if self.player_turn == player_1:
            self.board_array[rows-1-self.y, self.x] = 1
            self.start_row = rows-1-self.y +1
            self.start_column = self.x +1
        else:
            self.board_array[rows-1-self.y, self.x] = 2
            self.start_row = rows-1-self.y+1
            self.start_column = self.x+1
            print(self.start_row)

        self.x = 0
        self.y = 0
        print(self.board_array)
        self.next_turn()

       
        
    def on_draw(self):
        """ Called whenever we need to draw the window
        
        Input: Self
        Output: Drawing """
        arcade.start_render()
        board.draw_game_board()
        self.othello_piece_list.draw()
        self.show_score()
        self.check_winner()

       
rows= 1  
while rows < 4 or rows %2 ==1 :
    rows = int(input("Enter how many rows you want the game board to be (must begreater than 4 and even)"))

player_1 = str(input("Who wants to be player 1?"))
player_2 = str(input("Who wants to be player 2?"))
piece_size = int(250//rows)
board = Game_Board(arcade.color.FOREST_GREEN, rows)
def main():
    game = Othello()
    game.setup()
    arcade.run()
if __name__ == "__main__":
    main()