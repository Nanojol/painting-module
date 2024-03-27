import simple_draw as sd


def triangle(start_x, start_y, angle, length, width):
    point = sd.get_point(start_x, start_y)
    line = sd.get_vector(point, angle, length, width)
    line.draw()
    line = sd.get_vector(line.end_point, angle + 120, length, width)
    line.draw()
    line = sd.get_vector(line.end_point, angle + 240, length, width)
    line.draw()
