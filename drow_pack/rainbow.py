import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


def rainbow(rad, first_pointx, first_pointy):
    for colours in rainbow_colors:
        rad += 50
        point = sd.get_point(300, -50)
        sd.circle(point, rad, colours, 50)
