import arcade
import pyglet

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Othello"
SCALING = 2.0


class OthelloPiece():
    def __init__(self, color, size, x, y):
        self.color = color
        self.size = size
        self.x = x
        self.y = y

        
        
        
    def create_game_piece(self):
        """ 
        Creates black or white game piece

        Input: Self, String
        Output: 
        """
        print("pernid")
        arcade.draw_circle_filled(center_x=self.x, center_y=self.y, radius=self.size, color=self.color)
        
        

        


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
        self.player_list = None
        self.wall = None
        
    def setup(self):
        self.player_list = arcade.SpriteList()  


    
    def place_piece(self):
       pass

    def show_score(self):
        pass
    def next_turn(self):
        pass
    def determine_first_player(self):
        pass
    def flip_pieces(self):
        pass
    def winner(self):
        pass
    def start(self):
        pass

    def draw_game_board(self):
        pass
    def on_mouse_press(self, x, y, button, modifiers):
        self.wall = arcade.Sprite(":resources:images/tiles/grassMid.png", 1)
        self.wall.center_x = x
        self.wall.center_y = y
        self.wall.draw()
        self.player_list.append(self.wall)
       
        
    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        board.draw_game_board()
        self.player_list.draw()
       
        

rows = int(input("Enter how many rows you want the game board to be"))
piece_size = int(250//rows)
# Main code entry point
if __name__ == "__main__":
    game = Othello()
    game.setup()
    board = Game_Board(arcade.color.FOREST_GREEN, rows)
    
    arcade.run()