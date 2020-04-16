import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
TITLE = "Side Scroller"
GRAVITY = 1

  
class Player(arcade.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__('images/0.png',center_x = x, center_y = y)
        self.run_list = []
        self.jump_list = []
        self.slide_list = []
        for i in range(8, 16):
            self.run_list.append(arcade.load_texture(f'images/{i}.png'))
        for i in range(1,8):
            self.jump_list.append(arcade.load_texture(f'images/{i}.png'))
        
        self.slide_list.append(arcade.load_texture(f'images/S1.png'))
        for i in range(7):
            self.slide_list.append(arcade.load_texture(f'images/S2.png'))
        for i in range(3,6):
            self.slide_list.append(arcade.load_texture(f'images/S{i}.png'))
        
        self.jumping = False
        self.sliding = False
        self.slide_count = 0
        self.jump_count = 0
        self.run_count = 0
        self.slide_up = False
        self.speed = 1
    
    def draw(self):
        if self.jumping:
            self.texture = self.jump_list[self.jump_count // 18]
        elif self.sliding:
            self.texture = self.slide_list[self.slide_count // 10]
        else:
            self.texture = self.run_list[self.run_count // 6]
        
        super().draw()
        
        
    def update(self):
        if self.jumping:
            self.change_y -= 1
            self.jump_count += 1
            if self.jump_count >= 42:
                self.jump_count = 0
                self.jumping = False
                self.run_count = 0
                self.change_y = 0
            
        elif self.sliding or self.slide_up:
            if self.slide_count < 20:
                self.center_y -= 1
            elif self.slide_count == 80:
                self.center_y += 19
                self.sliding = False
                self.slide_up = True
            
            if self.slide_count >= 110:
                self.slide_count = 0
                self.slide_up = False
                self.run_count = 0
            self.slide_count += 1
            
            
        else:
            self.run_count += 1
            if self.run_count > 42:
                self.run_count = 0
                
        self.center_x += self.speed
        self.center_y += self.change_y
                
            
                              


class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
        
        
    def setup(self):
        self.player = Player(100, 100, 50, 50)
        self.saws = []
        self.bg = arcade.load_texture('images/bg.png')
        self.view_bottom = 0
        self.view_left = 0
        self.bg_x = 0
        self.bg_x2 = SCREEN_WIDTH
           
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(self.bg_x, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        arcade.draw_lrwh_rectangle_textured(self.bg_x2, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        self.player.draw()
        
    def on_update(self, delta_time):
        self.player.update()
        
        self.view_left += self.player.speed
        self.set_viewport(self.view_left, self.view_left + SCREEN_WIDTH,
                          self.view_bottom, self.view_bottom + SCREEN_HEIGHT)
        
        if self.view_left > self.bg_x + SCREEN_WIDTH:
            self.bg_x += 2*SCREEN_WIDTH
            
        if self.view_left > self.bg_x2 + SCREEN_WIDTH:
            self.bg_x2 += 2*SCREEN_WIDTH
        
    
    def on_key_press(self, key, modifier):
        if key == arcade.key.UP:
            self.player.change_y = 21
            self.player.jumping = True
        if key == arcade.key.DOWN:
            self.player.sliding = True
    
    def on_key_release(self, key, modifier):
        pass
    


def main():
    game = Game()
    game.setup()
    arcade.run()
    
if __name__ == "__main__":
    main()
        