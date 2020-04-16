import arcade

arcade.open_window(600, 600, "My Cool House")

# set sky color
arcade.set_background_color(arcade.color.SKY_BLUE)

# start drawing
arcade.start_render()

# draw ground
arcade.draw_lrtb_rectangle_filled(0, 600, 100, 0,arcade.color.GREEN)

# draw sun
arcade.draw_circle_filled(0, 600, 100, arcade.color.YELLOW)

# draw house
arcade.draw_lrtb_rectangle_filled(100, 500, 300, 100, arcade.color.RED)

# draw roof
arcade.draw_triangle_filled(100, 300, 500, 300, 300, 400, arcade.color.BLACK)

# draw door
arcade.draw_lrtb_rectangle_filled(275, 325, 180, 100, arcade.color.BROWN)

# draw door knob
arcade.draw_circle_filled(315, 135, 5, arcade.color.BLACK)

# draw left window
arcade.draw_rectangle_filled(200, 200, 50, 50, arcade.color.WHITE)
arcade.draw_rectangle_outline(200, 200, 50, 50, arcade.color.BLACK)
arcade.draw_line(200, 175, 200, 225, arcade.color.BLACK)
arcade.draw_line(175, 200, 225, 200, arcade.color.BLACK)

# draw right window
arcade.draw_rectangle_filled(400, 200, 50, 50, arcade.color.WHITE)
arcade.draw_rectangle_outline(400, 200, 50, 50, arcade.color.BLACK)
arcade.draw_line(400, 175, 400, 225,arcade.color.BLACK)
arcade.draw_line(375, 200, 425, 200,arcade.color.BLACK)

# draw clouds 
arcade.draw_circle_filled(50, 450, 50,arcade.color.WHITE)
arcade.draw_circle_filled(100, 450, 50,arcade.color.WHITE)
arcade.draw_circle_filled(200, 525, 50, arcade.color.WHITE)
arcade.draw_circle_filled(250, 525, 50, arcade.color.WHITE)

# finish drawing
arcade.finish_render()

arcade.run()