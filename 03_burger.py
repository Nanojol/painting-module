# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

import my_burger
# рецепт бургера спанч боб
# Булочки разрезать на две части.
# Смазать майонезом.
# Выложить котлету.
# На котлету выложить сыр.
# На сыр выложить помидор.
# На помидор выложить огурцы.
# Накрыть верхней частью булочк
burger = []

my_burger.bread(burger)
my_burger.mayo(burger)
my_burger.meatball(burger)
my_burger.cheese(burger)
my_burger.tomato(burger)
my_burger.cucumber(burger)
my_burger.bread(burger)

print(burger)

