import arcade

class MessageBox:
    def __init__(self, message, center_x, center_y, color, is_visible):
        self.message = message
        self.center_x = center_x
        self.center_y = center_y
        self.color = (color[0],color[1],color[2],200) # semi-transparent?
        self.width = len(message)*50 + 30
        self.height = 200
        self.is_visible = is_visible
        
    
    def draw(self):
        if self.is_visible:
            arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)
            arcade.draw_text(self.message, self.center_x, self.center_y, (0,0,0),20,align='center',anchor_x='center')
        

    def check_clicked(self, x, y):
        return x >= self.center_x - self.width/2 and x <= self.center_x + self.width/2 and \
               y >= self.center_y - self.height/2 and y <= self.center_y + self.height/2
            

        