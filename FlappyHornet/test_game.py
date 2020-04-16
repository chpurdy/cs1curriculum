import arcade
from gravity_play import Hornet

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class TestGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Test")
        arcade.set_background_color(arcade.color.GREEN)
        self.gravity = .5
        self.ground_level = 100
        
    def setup(self):
        self.h = Hornet()
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_xywh_rectangle_filled(0,0,SCREEN_WIDTH,self.ground_level,arcade.color.BROWN)
        self.h.draw()
        
    def on_update(self, delta_time):
        self.h.update_animation()
        self.h.update()
        
        if self.h.center_y > self.ground_level:
            self.h.change_y -= self.gravity
            
        else:
            self.h.center_y = self.ground_level
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.h.jump()
            
        if key == arcade.key.RIGHT:
            self.h.change_x += 5
            #self.h.state = arcade.FACE_RIGHT
            
        if key == arcade.key.LEFT:
            self.h.change_x += -5
            #self.h.state = arcade.FACE_LEFT
            
#     def on_key_release(self, key, modifiers):
#         if key == arcade.key.RIGHT:
#             self.h.change_x = 0
#             
#         if key == arcade.key.LEFT:
#             self.h.change_x = 0
    

def main():
    game = TestGame()
    game.setup()
    arcade.run()
    
if __name__ == "__main__":
    main()
    
    
    