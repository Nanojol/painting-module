# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1800, 600)


def wall(x, y):
    for _ in range(3):
        start_x = x

        down_point = sd.get_point(x, y)
        upper_point = sd.get_point(x + 100, y + 50)
        sd.rectangle(down_point, upper_point, (127, 63, 0), 6)
        for count in range(5):
            down_point = sd.get_point(x, y)
            upper_point = sd.get_point(x + 100, y + 50)
            x += 100
            sd.rectangle(down_point, upper_point, (127, 63, 0), 8)
        x = start_x-50
        y += 50
        down_point = sd.get_point(x, y)
        upper_point = sd.get_point(x + 100, y + 50)
        sd.rectangle(down_point, upper_point, (127, 63, 0), 8)
        for count in range(5):
            down_point = sd.get_point(x, y)
            upper_point = sd.get_point(x + 100, y + 50)
            x += 100
            sd.rectangle(down_point, upper_point, (127, 63, 0), 8)
        x = start_x
        y += 50





