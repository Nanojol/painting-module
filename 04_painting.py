# -*- coding: utf-8 -*-

import simple_draw as sd

from drow_pack.snowfall import snowfall
from drow_pack.snowfall import random_values_snow
from drow_pack.tree import draw_branches_v3
from drow_pack.house.house import *
from drow_pack.smile import smile
from drow_pack.rainbow import rainbow

sd.resolution = (1800, 600)

N = 4

sd.resolution = (1800, 600)
sd.start_drawing()
full_house(600, 0)
rainbow(1000, 1000, 50)
draw_branches_v3(1300, 30, 90, 32, 100)
smile(1200, 100)

random_values_snow()
snowfall(5)

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)
