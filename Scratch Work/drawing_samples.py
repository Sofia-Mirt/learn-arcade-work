"""
This is a sample program to show how to draw using
the Python programming language and the Arcade library.
"""

# Import the "arcade" library.
import arcade

# Open a window with a given size in pixels and title.
arcade.open_window(600, 600, "Drawing Example")

# Keep the window up until someone closes it.
arcade.run()

# Tell the Arcade library you are about to start drawing.
arcade.start_render()

# Set the background color.
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Tell the Arcade library you are done drawing.
arcade.finish_render()
