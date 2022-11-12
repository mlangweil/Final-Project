import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Othello"
SCALING = 2.0


class OthelloPiece():
    def __init__(self, color):
        self.color = color
    def create_game_piece(self, color):
        """ 
        Creates black or white game piece

        Input: Self, String
        Output: 
        """

        


class Game_Board():
    def __init__(self, color, rows):
        self.color = color
        self.rows = rows
    def draw_game_board(self):
        arcade.draw_rectangle_filled(400, 400, 400, 400, arcade.color.FOREST_GREEN)
   

class Othello(arcade.Window):

    def __init__(self):
        """Initialize the game
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.WHITE)

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
    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        arcade.draw_rectangle_filled(400, 400, 400, 400, arcade.color.FOREST_GREEN)

# Main code entry point
if __name__ == "__main__":
    game = Othello()
    arcade.run()