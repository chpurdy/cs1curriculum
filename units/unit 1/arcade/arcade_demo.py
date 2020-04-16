import arcade
import random

arcade.open_window(600, 600, "Drawing Example")

# set sky color
arcade.set_background_color(arcade.color.SKY_BLUE)

def draw_outdoors():
    # draw ground
    arcade.draw_lrtb_rectangle_filled(0,600,100,0,arcade.color.GREEN)

    # draw sun
    arcade.draw_circle_filled(0,600,100,arcade.color.YELLOW)

def draw_house():
    # draw house
    arcade.draw_lrtb_rectangle_filled(100, 500, 300, 100, arcade.color.RED)
    
    # draw roof
    arcade.draw_triangle_filled(100,300,500,300,300,400,arcade.color.BLACK)

    # draw door
    arcade.draw_lrtb_rectangle_filled(275,325,180,100,arcade.color.BROWN)

    # draw door knob
    arcade.draw_circle_filled(315,135,5,arcade.color.BLACK)

    # draw left window
    arcade.draw_rectangle_filled(200,200,50,50,arcade.color.WHITE)
    arcade.draw_rectangle_outline(200,200,50,50,arcade.color.BLACK)
    arcade.draw_line(200,175,200,225,arcade.color.BLACK)
    arcade.draw_line(175,200,225,200,arcade.color.BLACK)

    # draw right window
    arcade.draw_rectangle_filled(400,200,50,50,arcade.color.WHITE)
    arcade.draw_rectangle_outline(400,200,50,50,arcade.color.BLACK)
    arcade.draw_line(400,175,400,225,arcade.color.BLACK)
    arcade.draw_line(375,200,425,200,arcade.color.BLACK)


# draw clouds in semi-random location in sky
def draw_clouds(cloud1_x, cloud2_x):
    arcade.draw_circle_filled(cloud1_x,450,50,arcade.color.WHITE)
    arcade.draw_circle_filled(cloud1_x + 50,450,50,arcade.color.WHITE)

    arcade.draw_circle_filled(cloud2_x,525,50,arcade.color.WHITE)
    arcade.draw_circle_filled(cloud2_x + 50,525,50,arcade.color.WHITE)


def on_draw(delta_time):
    arcade.start_render()
    draw_house()
    draw_outdoors()
    draw_clouds(on_draw.cloud1_x, on_draw.cloud2_x)
    on_draw.cloud1_x += 1
    on_draw.cloud2_x += 1
    on_draw.cloud1_x %= 625
    on_draw.cloud2_x %= 625
    
on_draw.cloud1_x = 50
on_draw.cloud2_x = 200

arcade.schedule(on_draw, 1/60)
arcade.run()