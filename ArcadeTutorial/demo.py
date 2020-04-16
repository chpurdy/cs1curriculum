import arcade

arcade.open_window(600, 600, "Polygons")

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

trap = ( (250, 200),
         (550, 200),
         (600, 100),
         (200, 100) )

arcade.draw_polygon_filled(trap, arcade.color.GREEN)

t_shape = ( (300, 400),
            (500, 400),
            (500, 350),
            (425, 350),
            (425, 300),
            (375, 300),
            (375, 350),
            (300, 350) )

arcade.draw_polygon_filled(t_shape, arcade.color.BLUE)




arcade.finish_render()

arcade.run()