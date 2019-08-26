import arcade
import random
# wasp art from https://opengameart.org/content/wasp-0
# swat and jump sound effect Recorded by Mike Koenig @ http://soundbible.com
# score sound recorded by Corsica @ http://soundbible.com/1424-Air-Plane-Ding.html

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
HORNET_JUMP_SPEED = 10

# Game state
GAME_OVER = 0
PLAYING = 1
START = 2


class FlappyHornet(arcade.Window):
    
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Lists to keep track of sprites
        self.swatter_list = None
        self.hornet_list = None
        self.table_list = None
        self.score = None
        # Keep track of player sprite
        # Set up the player hornet
        self.hornet_sprite = arcade.AnimatedTimeSprite()
              
        # Load animated textures
        self.hornet_sprite.textures = []
        self.hornet_sprite.textures.append(arcade.load_texture("assets/images/wasp-0.png",scale=CHARACTER_SCALING))
        self.hornet_sprite.textures.append(arcade.load_texture("assets/images/wasp-1.png",scale=CHARACTER_SCALING))
        
        # Load sounds
        self.swat_sound = arcade.load_sound("assets/sounds/swat.mp3")
        self.jump_sound = arcade.load_sound("assets/sounds/jump.mp3")
        self.score_sound = arcade.load_sound("assets/sounds/score.mp3")
        
        
        self.state = None
        self.scroll_speed = None  # adjust difficulty?
        
        arcade.set_background_color(arcade.color.SKY_BLUE)
        
        
        
    
    def setup(self):
        """
        Set up the game.  Call this function to restart the game.
        """
        
        # Create sprite lists
        self.hornet_list = arcade.SpriteList()
        self.swatter_list = arcade.SpriteList()
        self.table_list = arcade.SpriteList() 
        
        self.scroll_speed = 2
        self.score = 0
        self.state = START
        
        # Set up the player hornet
        
        self.hornet_sprite.center_x = 64
        self.hornet_sprite.center_y = SCREEN_HEIGHT // 2
        
              
        # Put sprite into list to be drawn
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
            bottom_y = random.randint(0,200)
            bottom_swatter = arcade.Sprite("assets/images/swatter.png", SWATTER_SCALING)
            bottom_swatter.center_x = x
            bottom_swatter.center_y = bottom_y
            bottom_swatter.angle = 180
            bottom_swatter.scored = False
            self.swatter_list.append(bottom_swatter)
            top_swatter = arcade.Sprite("assets/images/swatter.png", SWATTER_SCALING)
            top_swatter.center_x = x
            top_swatter.center_y = bottom_y + 800
            top_swatter.scored = False
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
        
        score_text = f"Score: {int(self.score)}"
        arcade.draw_text(score_text, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 40, arcade.color.MAROON,18)
        
        if self.state == START:
            arcade.draw_text("Welcome to Flappy Hornet!",SCREEN_WIDTH//4, SCREEN_HEIGHT//2+100, arcade.color.MAROON,20)
            arcade.draw_text("Press 'R' to begin the game",SCREEN_WIDTH//4, SCREEN_HEIGHT//2+50, arcade.color.MAROON,20)
            
        if self.state == GAME_OVER:
            arcade.draw_text("Press 'R' to restart",SCREEN_WIDTH//4, SCREEN_HEIGHT//2+50, arcade.color.MAROON,20)
        
    
    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.SPACE and self.state == PLAYING:
            self.hornet_sprite.change_y = HORNET_JUMP_SPEED
        
        if key == arcade.key.R and self.state == GAME_OVER:
            self.setup()
            
        if key == arcade.key.R and self.state == START:
            self.state = PLAYING
            
    
    def on_key_release(self, key, modifiers):
        """
        Called when user releases a key.
        """
        if key == arcade.key.SPACE:
            self.hornet_sprite.change_y = 0
            
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when mouse button clicked
        """
        if button == arcade.MOUSE_BUTTON_LEFT and self.state == PLAYING:
            self.hornet_sprite.change_y = HORNET_JUMP_SPEED
            self.jump_sound.play()
            
            
    
    
    def update(self, delta_time):
        """
        Movement and game logic
        """
        self.hornet_list.update_animation()
        
        
        
        if self.state == PLAYING:
            for swatter in self.swatter_list:
                swatter.center_x -= self.scroll_speed
                if swatter.center_x <= self.hornet_sprite.center_x and not swatter.scored:
                    self.score += 0.5
                    swatter.scored = True
                    if self.score == int(self.score):
                        self.score_sound.play()
                    print(self.score)
                    
                if swatter.center_x <= -100: # off screen?
                     self.swatter_list.remove(swatter)
            self.physics_engine.update()
            
            for swatter in self.swatter_list:
                if swatter.collides_with_sprite(self.hornet_sprite):
                    if swatter.center_y + swatter.collision_radius > self.hornet_sprite.center_y - self.hornet_sprite.collision_radius:
                        self.swat_sound.play()
                        self.state = GAME_OVER
                        print("GAME OVER")
            
                

def main():
    window = FlappyHornet()
    window.setup()
    arcade.run()
    
if __name__ == "__main__":
    main()
        