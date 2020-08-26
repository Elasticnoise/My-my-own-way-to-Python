# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1 import room1 as central_h1_rm1
from district.central_street.house1 import room2 as central_h1_rm2
from district.central_street.house2 import room1 as central_h2_rm1
from district.central_street.house2 import room2 as central_h2_rm2
from district.soviet_street.house1 import room1 as soviet_h1_rm1
from district.soviet_street.house1 import room2 as soviet_h1_rm2
from district.soviet_street.house2 import room1 as soviet_h2_rm1
from district.soviet_street.house2 import room2 as soviet_h2_rm2


total_residents_list = (
    central_h1_rm1.folks
    + central_h1_rm2.folks + central_h2_rm1.folks
    + central_h2_rm2.folks + soviet_h1_rm1.folks
    + soviet_h1_rm2.folks + soviet_h2_rm1.folks
    + soviet_h2_rm2.folks
)
comma = ', '
residents = comma.join(total_residents_list)
print('На районе живут', residents)

# зачет!
