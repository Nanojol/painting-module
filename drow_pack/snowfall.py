# -*- coding: utf-8 -*-

import simple_draw as sd
import random



def random_values_snow():
    return {

        'start_x': random.randrange(50, 500),
        'start_y': random.randrange(500, 650, 50),
        'a_list': random.randrange(1, 8) / 10,
        'b_list': random.randrange(1, 8) / 10,
        'c_list': random.randrange(30, 60),
        'length_list': random.randrange(20, 50),

    }

def snowfall(N):

    all_random_values = []

    for _ in range(N):
        all_random_values.append(random_values_snow())

    sd.start_drawing()


    while True:
        # sd.clear_screen()
        for i in all_random_values:

            point_starter = sd.get_point(i['start_x'], i['start_y'])
            sd.snowflake(point_starter, i['length_list'], sd.background_color, i['a_list'], i['b_list'], i['c_list'])

            i['start_y'] -= 10
            if i['start_y'] < 1:
                all_random_values.remove(i)
            i['start_x'] -= sd.randint(-10, 10)

            point_starter = sd.get_point(i['start_x'], i['start_y'])
            sd.snowflake(point_starter, i['length_list'], sd.COLOR_WHITE, i['a_list'], i['b_list'], i['c_list'])

        all_random_values.append(random_values_snow())

        sd.finish_drawing()

        sd.sleep(0.1)
        if sd.user_want_exit():
            break

