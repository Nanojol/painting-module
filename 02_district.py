# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

import district.central_street.house1.room1
import district.central_street.house1.room2
import district.central_street.house2.room1
import district.central_street.house2.room2
import district.soviet_street.house1.room1
import district.soviet_street.house1.room2
import district.soviet_street.house2.room1
import district.soviet_street.house2.room2



people =[
*district.central_street.house1.room1.folks,
*district.central_street.house1.room2.folks,
*district.central_street.house2.room1.folks,
*district.central_street.house2.room2.folks,
*district.soviet_street.house1.room1.folks,
*district.soviet_street.house1.room2.folks,
*district.soviet_street.house2.room1.folks,
*district.soviet_street.house2.room2.folks
]

print('На районе живут ', *people, sep=",")




