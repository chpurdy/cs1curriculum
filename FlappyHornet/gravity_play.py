
import arcade



class Hornet(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()
        
        texture = arcade.load_texture('assets/images/wasp-0.png')
        self.texture = texture
        self.walk_right_textures.append(texture)
        self.stand_right_textures.append(texture)
        texture = arcade.load_texture('assets/images/wasp-1.png')
        self.walk_right_textures.append(texture)
        texture = arcade.load_texture('assets/images/wasp-0.png',mirrored=True)
        self.walk_left_textures.append(texture)
        self.stand_left_textures.append(texture)
        texture = arcade.load_texture('assets/images/wasp-1.png',mirrored=True)
        self.walk_left_textures.append(texture)
    
        self.scale = 2
        
 
        

            
        
           
        
    
    def jump(self):
        self.change_y = 6