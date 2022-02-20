"""
This is my program to practice how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the dimensions (width and height)
# Set the window title to "Drawing Example"
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.WHITE)

# Get ready to draw
arcade.start_render()

# --- Draw the race track ---

# Draw the limits of the race track
arcade.draw_rectangle_filled(0, 550, 75, 50, arcade.csscolor.RED)
arcade.draw_rectangle_filled(150, 550, 75, 50, arcade.csscolor.RED)
arcade.draw_rectangle_filled(300, 550, 75, 50, arcade.csscolor.RED)
arcade.draw_rectangle_filled(450, 550, 75, 50, arcade.csscolor.RED)
arcade.draw_rectangle_filled(600, 550, 75, 50, arcade.csscolor.RED)

arcade.draw_lrtb_rectangle_filled(0, 600, 520, 0, arcade.color.BLACK)

# Draw the limits of the race track
arcade.draw_lrtb_rectangle_filled(0, 600, 53, 0, arcade.color.WHITE)
arcade.draw_rectangle_filled(0, 0, 75, 100, arcade.csscolor.RED)
arcade.draw_rectangle_filled(150, 0, 75, 100, arcade.csscolor.RED)
arcade.draw_rectangle_filled(300, 0, 75, 100, arcade.csscolor.RED)
arcade.draw_rectangle_filled(450, 0, 75, 100, arcade.csscolor.RED)
arcade.draw_rectangle_filled(600, 0, 75, 100, arcade.csscolor.RED)

# --- Draw Mercedes-Benz car ---
arcade.draw_triangle_filled(500, 400, 600, 400, 500, 450, arcade.csscolor.DARK_GRAY)
arcade.draw_triangle_filled(325, 450, 425, 475, 425, 450, arcade.csscolor.DARK_GRAY)
arcade.draw_rectangle_filled(400, 425, 200, 50, arcade.csscolor.DARK_GRAY)

# Front wheel
arcade.draw_circle_filled(500, 400, 30, arcade.csscolor.DIM_GRAY)
arcade.draw_circle_filled(500, 400, 25, arcade.csscolor.GOLD)
arcade.draw_circle_filled(500, 400, 22, arcade.csscolor.WHITE)
arcade.draw_circle_filled(500, 400, 19, arcade.csscolor.SILVER)

# Rear wheel
arcade.draw_circle_filled(350, 400, 30, arcade.csscolor.DIM_GRAY)
arcade.draw_circle_filled(350, 400, 25, arcade.csscolor.GOLD)
arcade.draw_circle_filled(350, 400, 22, arcade.csscolor.WHITE)
arcade.draw_circle_filled(350, 400, 19, arcade.csscolor.SILVER)

# Draw text at (370, 425) with a font size of 12 pts
arcade.draw_text("Mercedes-Benz", 370, 425, arcade.color.BLACK, 12)

# --- Draw Ferrari car ---
arcade.draw_triangle_filled(350, 250, 450, 250, 350, 300, arcade.csscolor.RED)
arcade.draw_triangle_filled(175, 300, 275, 325, 275, 300, arcade.csscolor.RED)
arcade.draw_rectangle_filled(250, 275, 200, 50, arcade.csscolor.RED)

# Front wheel
arcade.draw_circle_filled(350, 250, 30, arcade.csscolor.DIM_GRAY)
arcade.draw_circle_filled(350, 250, 25, arcade.csscolor.GOLD)
arcade.draw_circle_filled(350, 250, 22, arcade.csscolor.WHITE)
arcade.draw_circle_filled(350, 250, 19, arcade.csscolor.SILVER)

# Rear wheel
arcade.draw_circle_filled(200, 250, 30, arcade.csscolor.DIM_GRAY)
arcade.draw_circle_filled(200, 250, 25, arcade.csscolor.GOLD)
arcade.draw_circle_filled(200, 250, 22, arcade.csscolor.WHITE)
arcade.draw_circle_filled(200, 250, 19, arcade.csscolor.SILVER)

# Draw text at (250, 275) with a font size of 12 pts
arcade.draw_text("Ferrari", 250, 275, arcade.color.BLACK, 12)

# --- Draw Red Bull Racing ---
arcade.draw_triangle_filled(200, 100, 300, 100, 200, 150, arcade.csscolor.DARK_BLUE)
arcade.draw_triangle_filled(25, 150, 125, 150, 125, 175, arcade.csscolor.DARK_BLUE)
arcade.draw_rectangle_filled(100, 125, 200, 50, arcade.csscolor.DARK_BLUE)

# Front wheel
arcade.draw_circle_filled(200, 100, 30, arcade.csscolor.DIM_GRAY)
arcade.draw_circle_filled(200, 100, 25, arcade.csscolor.GOLD)
arcade.draw_circle_filled(200, 100, 22, arcade.csscolor.WHITE)
arcade.draw_circle_filled(200, 100, 19, arcade.csscolor.SILVER)

# Rear wheel
arcade.draw_circle_filled(50, 100, 30, arcade.csscolor.DIM_GRAY)
arcade.draw_circle_filled(50, 100, 25, arcade.csscolor.GOLD)
arcade.draw_circle_filled(50, 100, 22, arcade.csscolor.WHITE)
arcade.draw_circle_filled(50, 100, 19, arcade.csscolor.SILVER)

# Draw text at (65, 125) with a font size of 12 pts
arcade.draw_text("Red Bull Racing", 65, 125, arcade.color.BLACK, 12)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
