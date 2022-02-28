# Import the "arcade" library
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_race_track():
    """ Draw the limits of the race track """
    arcade.draw_rectangle_filled(0, 550, 75, 50, arcade.csscolor.RED)
    arcade.draw_rectangle_filled(150, 550, 75, 50, arcade.csscolor.RED)
    arcade.draw_rectangle_filled(300, 550, 75, 50, arcade.csscolor.RED)
    arcade.draw_rectangle_filled(450, 550, 75, 50, arcade.csscolor.RED)
    arcade.draw_rectangle_filled(600, 550, 75, 50, arcade.csscolor.RED)
    arcade.draw_rectangle_filled(750, 550, 75, 50, arcade.csscolor.RED)

    arcade.draw_lrtb_rectangle_filled(0, 800, 520, 0, arcade.color.BLACK)

    arcade.draw_lrtb_rectangle_filled(0, 800, 53, 0, arcade.color.WHITE)

    arcade.draw_rectangle_filled(0, 0, 75, 100, arcade.csscolor.RED)
    arcade.draw_rectangle_filled(150, 0, 75, 100, arcade.csscolor.RED)
    arcade.draw_rectangle_filled(300, 0, 75, 100, arcade.csscolor.RED)
    arcade.draw_rectangle_filled(450, 0, 75, 100, arcade.csscolor.RED)
    arcade.draw_rectangle_filled(600, 0, 75, 100, arcade.csscolor.RED)
    arcade.draw_rectangle_filled(750, 0, 75, 100, arcade.csscolor.RED)


def draw_Mercedes_Benz_car(x, y):
    """ Draw Mercedes-Benz car """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.WHITE, 5)

    # Draw Mercedes-Benz car
    arcade.draw_triangle_filled(50 + x, 400, 150 + x, 400, 50 + x, 450, arcade.csscolor.DARK_GRAY)
    arcade.draw_triangle_filled(x - 125, 450, x - 25, 475, x - 25, 450, arcade.csscolor.DARK_GRAY)
    arcade.draw_rectangle_filled(x - 50, 425, 200, 50, arcade.csscolor.DARK_GRAY)

    # Front wheel
    arcade.draw_circle_filled(50 + x, 400, 30, arcade.csscolor.DIM_GRAY)
    arcade.draw_circle_filled(50 + x, 400, 25, arcade.csscolor.GOLD)
    arcade.draw_circle_filled(50 + x, 400, 22, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(50 + x, 400, 19, arcade.csscolor.SILVER)

    # Rear wheel
    arcade.draw_circle_filled(x - 100, 400, 30, arcade.csscolor.DIM_GRAY)
    arcade.draw_circle_filled(x - 100, 400, 25, arcade.csscolor.GOLD)
    arcade.draw_circle_filled(x - 100, 400, 22, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x - 100, 400, 19, arcade.csscolor.SILVER)

    # Draw text at (370, 425) with a font size of 12 pts
    arcade.draw_text("Mercedes-Benz", x - 80, 425, arcade.color.BLACK, 12)


def draw_Ferrari_car(x, y):
    """ Draw Ferrari car """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.WHITE, 5)

    # Draw Ferrari car
    arcade.draw_triangle_filled(50 + x, 250, 150 + x, 250, 50 + x, 300, arcade.csscolor.RED)
    arcade.draw_triangle_filled(x - 125, 300, x - 25, 325, x - 25, 300, arcade.csscolor.RED)
    arcade.draw_rectangle_filled(x - 50, 275, 200, 50, arcade.csscolor.RED)

    # Front wheel
    arcade.draw_circle_filled(50 + x, 250, 30, arcade.csscolor.DIM_GRAY)
    arcade.draw_circle_filled(50 + x, 250, 25, arcade.csscolor.GOLD)
    arcade.draw_circle_filled(50 + x, 250, 22, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(50 + x, 250, 19, arcade.csscolor.SILVER)

    # Rear wheel
    arcade.draw_circle_filled(x - 100, 250, 30, arcade.csscolor.DIM_GRAY)
    arcade.draw_circle_filled(x - 100, 250, 25, arcade.csscolor.GOLD)
    arcade.draw_circle_filled(x - 100, 250, 22, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x - 100, 250, 19, arcade.csscolor.SILVER)

    # Draw text at (250, 275) with a font size of 12 pts
    arcade.draw_text("Ferrari", x - 50, 275, arcade.color.BLACK, 12)


def draw_Red_Bull_Racing_car(x, y):
    """ Draw Red Bull Racing car """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.WHITE, 5)

    # Draw Red Bull Racing
    arcade.draw_triangle_filled(50 + x, 100, 150 + x, 100, 50 + x, 150, arcade.csscolor.DARK_BLUE)
    arcade.draw_triangle_filled(x - 125, 150, x - 25, 150, x - 25, 175, arcade.csscolor.DARK_BLUE)
    arcade.draw_rectangle_filled(x - 50, 125, 200, 50, arcade.csscolor.DARK_BLUE)

    # Front wheel
    arcade.draw_circle_filled(50 + x, 100, 30, arcade.csscolor.DIM_GRAY)
    arcade.draw_circle_filled(50 + x, 100, 25, arcade.csscolor.GOLD)
    arcade.draw_circle_filled(50 + x, 100, 22, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(50 + x, 100, 19, arcade.csscolor.SILVER)

    # Rear wheel
    arcade.draw_circle_filled(x - 100, 100, 30, arcade.csscolor.DIM_GRAY)
    arcade.draw_circle_filled(x - 100, 100, 25, arcade.csscolor.GOLD)
    arcade.draw_circle_filled(x - 100, 100, 22, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x - 100, 100, 19, arcade.csscolor.SILVER)

    # Draw text at (65, 125) with a font size of 12 pts
    arcade.draw_text("Red Bull Racing", x - 85, 125, arcade.color.BLACK, 12)


def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    draw_race_track()
    draw_Mercedes_Benz_car(on_draw.Mercedes_Benz_car_x, 397)
    draw_Ferrari_car(on_draw.Ferrari_car_x, 247)
    draw_Red_Bull_Racing_car(on_draw.Red_Bull_Racing_car_x, 97)

    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.
    on_draw.Mercedes_Benz_car_x += 1
    on_draw.Ferrari_car_x += 1
    on_draw.Red_Bull_Racing_car_x += 1


# Create a value that our on_draw.Mercedes_Benz_car_x will start at.
on_draw.Mercedes_Benz_car_x = 450

# Create a value that our on_draw.Ferrari_car_x will start at.
on_draw.Ferrari_car_x = 300

# Create a value that our on_draw.Red_Bull_Racing_car_x will start at.
on_draw.Red_Bull_Racing_car_x = 150


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.csscolor.WHITE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1 / 60)
    arcade.run()


# Call the main function to get the program started.
main()
