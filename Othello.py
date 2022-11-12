import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Othello"
SCALING = 2.0


class OthelloPiece():
    def __init__(self):
        pass
    def create_game_piece(self, color, position_x, position_y):
        """ 
        Creates black or white game piece

        Input: Self, String
        Output: 
        """
        self.color = color
        self.position_x = position_x
        self.position_y = position_y

        arcade.draw_circle_filled(position_x, position_y, 50, self.color)

        


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
        game_piece = OthelloPiece()
        white_piece = game_piece.create_game_piece(arcade.color.WHITE, 20, 40)
        black_piece = game_piece.create_game_piece(arcade.color.BLACK, 30, 50)


              
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

    def draw_game_board(self):
        pass
    def on_draw(self):
        """ Called whenever we need to draw the window. """

        arcade.start_render()
        board.draw_game_board()

rows = int(input("Enter how many rows you want the game board to be"))
# Main code entry point
if __name__ == "__main__":
    game = Othello()
    board = Game_Board(arcade.color.FOREST_GREEN, rows)
    arcade.run()