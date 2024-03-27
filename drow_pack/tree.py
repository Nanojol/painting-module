# -*- coding: utf-8 -*-
import math
import random
import simple_draw as sd


def draw_branches_v3(start_x, start_y, angle, variation, length):
    root_start_point = sd.get_point(start_x, start_y)
    root_angle = angle
    root_radian = (root_angle * math.pi) / 180
    root_end_y = math.sin(root_radian) * length
    root_end_x = math.cos(root_radian) * length
    root_last_point = sd.get_point(root_end_x + start_x, root_end_y + start_y)
    sd.line(root_start_point, root_last_point, width=2)

    if length < 1:
        return

    start_point = sd.get_point(root_last_point.x, root_last_point.y)
    left_angle = angle + variation
    left_radian = (left_angle * math.pi) / 180
    left_end_y = math.sin(left_radian) * length
    left_end_x = math.cos(left_radian) * length
    left_last_point = sd.get_point(left_end_x + root_last_point.x, left_end_y + root_last_point.y)
    sd.line(start_point, left_last_point, width=2)

    right_angle = angle - variation
    right_radian = (right_angle * math.pi) / 180
    right_end_y = math.sin(right_radian) * length
    right_end_x = math.cos(right_radian) * length
    right_last_point = sd.get_point(right_end_x + root_last_point.x, right_end_y + root_last_point.y)
    sd.line(start_point, right_last_point, width=2)

    draw_branches_v3(right_last_point.x, right_last_point.y, right_angle, variation,
                     length * random.randrange(6, 8) / 10)
    draw_branches_v3(left_last_point.x, left_last_point.y, left_angle, variation, length * random.randrange(6, 8) / 10)
