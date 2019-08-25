import arcade
import random
# wasp art from https://opengameart.org/content/wasp-0

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Flappy Hornet"

# constants for scaling sprites
CHARACTER_SCALING = 2
SWATTER_SCALING = 1.5
TABLE_SCALING = 1

# Speed constants
HORNET_MOVEMENT_SPEED = 5
GRAVITY = 1
HORNET_JUMP_SPEED = 15


class FlappyHornet(arcade.Window):
    
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Lists to keep track of sprites
        self.swatter_list = None
        self.hornet_list = None
        self.table_list = None
        self.score = None
        # Keep track of player sprite
        self.hornet_sprite = None
        
        self.scroll_speed = None  # adjust difficulty?
        
        arcade.set_background_color(arcade.color.SKY_BLUE)
        
        
        
    
    def setup(self):
        """
        Set up the game.  Call this function to restart the game.
        """
        
        # Create sprite lists
        self.hornet_list = arcade.SpriteList()
        self.swatter_list = arcade.SpriteList()
        self.table_list = arcade.SpriteList() # used for platforms
        
        self.scroll_speed = 2
        self.score = 0
        
        # Set up the player hornet
        self.hornet_sprite = arcade.Sprite("assets/images/wasp-0.png", CHARACTER_SCALING)
        self.hornet_sprite.center_x = 64
        self.hornet_sprite.center_y = SCREEN_HEIGHT // 2
        self.hornet_list.append(self.hornet_sprite)
        
        # add ground
        for x in range(0,2000,64):
            bottom_table = arcade.Sprite("assets/images/table.png", TABLE_SCALING)
            bottom_table.center_x = x
            bottom_table.center_y = 32 # half way
            self.table_list.append(bottom_table)
            top_table = arcade.Sprite("assets/images/table.png", TABLE_SCALING)
            top_table.center_x = x
            top_table.center_y = SCREEN_HEIGHT - 32 # half way
            self.table_list.append(top_table)
            
        
        
        # add swatters        
        for x in range(300, 10000, 400):
            bottom_y = random.randint(0,300)
            bottom_swatter = arcade.Sprite("assets/images/swatter.png", SWATTER_SCALING)
            bottom_swatter.center_x = x
            bottom_swatter.center_y = bottom_y
            bottom_swatter.angle = 180
            self.swatter_list.append(bottom_swatter)
            top_swatter = arcade.Sprite("assets/images/swatter.png", SWATTER_SCALING)
            top_swatter.center_x = x
            top_swatter.center_y = bottom_y + 700
            self.swatter_list.append(top_swatter)
            
        
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.hornet_sprite,
                                                             self.table_list,
                                                             GRAVITY)
        
        
        
    def on_draw(self):
        """
        Render the screen.
        """
        
        arcade.start_render()
        self.table_list.draw()
        self.hornet_list.draw()
        self.swatter_list.draw()
        
    
    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.SPACE:
            self.hornet_sprite.change_y = HORNET_JUMP_SPEED
        
    
    def on_key_release(self, key, modifiers):
        """
        Called when user releases a key.
        """
        if key == arcade.key.SPACE:
            self.hornet_sprite.change_y = 0
            
    
    def update(self, delta_time):
        """
        Movement and game logic
        """
        
        for swatter in self.swatter_list:
            swatter.center_x -= self.scroll_speed
            if swatter.center_x <= self.hornet_sprite.center_x:
                self.score += 0.5
                self.swatter_list.remove(swatter)
                print(self.score)
        self.physics_engine.update()
        
        for swatter in self.swatter_list:
            if swatter.collides_with_sprite(self.hornet_sprite):
                print(swatter.collision_radius)
                print(self.hornet_sprite.collision_radius)
                print("GAME OVER")
                arcade.pause(.5)
                

def main():
    window = FlappyHornet()
    window.setup()
    arcade.run()
    
if __name__ == "__main__":
    main()
        