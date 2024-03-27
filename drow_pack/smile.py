# -*- coding: utf-8 -*-


import simple_draw as sd


def smile(cord_x, cord_y):
    point = sd.get_point(cord_x, cord_y)
    sd.circle(point, 100, sd.COLOR_DARK_GREEN, 5)
    eyes_left = sd.get_point(cord_x - 35, cord_y + 20)
    eyes_right = sd.get_point(cord_x + 30, cord_y + 20)
    sd.circle(eyes_left, 10, sd.COLOR_DARK_GREEN, 5)
    sd.circle(eyes_right, 30, sd.COLOR_DARK_GREEN, 5)
    mouth_point_bot = sd.get_point(cord_x - 70, cord_y - 80)
    mouth_point_top = sd.get_point(cord_x + 20, cord_y - 20)
    sd.ellipse(mouth_point_bot, mouth_point_top, sd.COLOR_DARK_GREEN, 0)



