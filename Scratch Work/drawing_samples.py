"""
This is a sample program to show how to draw using
the Python programming language and the Arcade library.
"""

# Import the "arcade" library.
import arcade

# Open a window with a given size in pixels and title.
arcade.open_window(600, 600, "Drawing Example")

# Set the background color.
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Tell the Arcade library you are about to start drawing.
arcade.start_render()

# Draw a rectangle.
# Left of 0, right of 599.
# Top of 300, bottom of 0.
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

# Three trunk.
# Center of 100, 320 (Центр прямоугольника по оси X и по оси Y).
# Width of 20.
# Height of 60.
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)

# Tree top (Центр круга, радиус, цвет).
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

# Another tree, with an ellipse for the top.
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)

# Another tree, with a trunk and arc for the top.
# Arc is centered at (300, 340) with a width of 60 and height of 100.
# The starting angle is0/ and ending is 180.
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

# Another tree, with a trunk and triangle for the top.
# Triangle is made of these points:
# (400, 400), (370, 320), (430, 320).
arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)

# Draw a tree using a polygon with a list of points.
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 400),
                            (480, 360),
                            (470, 320),
                            (530, 320),
                            (520, 360)
                            ),
                           arcade.csscolor.DARK_GREEN)

# Draw a sun.
arcade.draw_circle_filled(500, 550, 40, arcade.csscolor.ORANGE)

# Rays to the left, right, up and down.
arcade.draw_line(500, 550, 400, 550, arcade.csscolor.ORANGE, 3)
arcade.draw_line(500, 550, 600, 550, arcade.csscolor.ORANGE, 3)
arcade.draw_line(500, 550, 500, 450, arcade.csscolor.ORANGE, 3)
arcade.draw_line(500, 550, 500, 650, arcade.csscolor.ORANGE, 3)

# Diagonal rays.
arcade.draw_line(500, 550, 550, 600, arcade.csscolor.ORANGE, 3)
arcade.draw_line(500, 550, 550, 500, arcade.csscolor.ORANGE, 3)
arcade.draw_line(500, 550, 450, 500, arcade.csscolor.ORANGE, 3)
arcade.draw_line(500, 550, 450, 600, arcade.csscolor.ORANGE, 3)

#
arcade.draw_text("Arbor Day - Plant a Tree!",
                 150, 230,
                 arcade.csscolor.BLACK, 24)

# Tell the Arcade library you are done drawing.
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
