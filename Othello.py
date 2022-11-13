import arcade
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Othello"
SCALING = 2.0



        

class Game_Board():
    def __init__(self, color, rows):
        self.color = color
        self.rows = rows
       

       
    def draw_game_board(self):
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
        """Initialize the game
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.WHITE) 
        self.othello_piece_list = None
        self.black_piece = None
        self.black_score = 0
        self.white_score = 0
        self.player_turn = ""
        self.player_1_moves = 0
        self.player_2_moves = 0

        
    def setup(self):
        self.othello_piece_list = arcade.SpriteList()  


    
    def place_piece(self):
       pass

    def show_score(self):
        arcade.draw_text("Score:" + str(score), 483, 405, arcade.color.BLACK, 12)

    def next_turn(self):
        pass
    def determine_first_player(self):
        self.first_player_choose = random.randint(0,1)
        if self.first_player_choose == 1:
            self.player_1_turn()
        else:
            self.player_2_turn()


    def flip_pieces(self):
        pass
    def check_winner(self):
        if self.black_score > self.white_score:
            pass
        elif self.white_score > self.black_score:
            pass
        else:
            pass
    def player_1_turn(self):
        pass
    def player_2_turn(self):
        pass

    def draw_game_board(self):
        pass
    def on_mouse_press(self, x, y, button, modifiers):
        self.black_piece = arcade.Sprite(":resources:onscreen_controls/shaded_dark/unchecked.png", piece_size/25)
        self.black_piece.center_x = x
        self.black_piece.center_y = y
        self.othello_piece_list.append(self.black_piece)
        if self.first_player_choose == 1:
            self.player_1_moves +=1
            self.check_winner()

            self.player_2_turn = "PLAYER2"

        else:
            self.player_2_turn()
            self.player_2_moves +=1
            self.check_winner()

            self.player_1_turn = "PLAYER1"



       
        
    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        board.draw_game_board()
        self.othello_piece_list.draw()
       
        

rows = int(input("Enter how many rows you want the game board to be."))
piece_size = int(250//rows)
board = Game_Board(arcade.color.FOREST_GREEN, rows)
def main():
    game = Othello()
    game.setup()
    arcade.run()
if __name__ == "__main__":
    main()