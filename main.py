from pprint import pprint
import os
from dec import dec, path_dec

path = os.path.join(os.getcwd(), 'recipes.txt')

with open(path, encoding='utf-8') as file:
    res = {}
    for dish in file:
        dish_name = dish.strip()
        counter = int(file.readline().strip())
        temp = []
        for item in range(counter):
            ingredient_name, quantity, measure = file.readline().split('|')
            temp.append(
                {'ingredient_name': ingredient_name.strip(),
                 'quantity': int(quantity.strip()),
                 'measure': measure.strip()}
            )
        res[dish_name] = temp
        file.readline()
print()
# =========case1 complete==========


@dec(path_dec)
def get_shop_list_by_dishes(dishes, person_count):
    if person_count <= 0:
        return 'Неверное количество персон'
    result = {}
    if type(dishes) == str:
        if dishes.capitalize() in res.keys():
            for ingredient in res[dishes.capitalize()]:
                result[ingredient['ingredient_name']] = \
                    {'measure': ingredient['measure'], 'quantity': (ingredient['quantity'])*person_count}
            return result
        else:
            return 'Блюдо отсутствует в списке'
    if type(dishes) == list:
        for _dish in dishes:
            if _dish.capitalize() in res.keys():
                for ingredient in res[_dish.capitalize()]:
                    if ingredient['ingredient_name'] in result.keys():
                        result[ingredient['ingredient_name']]['quantity'] += ingredient['quantity']*person_count
                    else:
                        result[ingredient['ingredient_name']] = \
                            {'measure': ingredient['measure'],
                             'quantity': (ingredient['quantity']) * person_count}
            else:
                return 'Блюдо отсутствует в списке'
        return result


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
print()
# =========case2 complete==========


path1 = os.getcwd()
list_files = []


@dec(path_dec)
def list_create(path=path1):
    directory = os.listdir(path)
    list_files.append(directory[directory.index('1.txt')])
    list_files.append(directory[directory.index('2.txt')])
    list_files.append(directory[directory.index('3.txt')])
    return list_files


@dec(path_dec)
def merged_files(list_files):
    list_names = []
    for item in list_files:
        counter = 0
        with open(item, encoding="utf-8") as file:
            for line in file:
                counter += 1
        list_names.append([item, counter])
    list_names.sort(key=lambda z: z[1])
    with open('result.txt', 'w', encoding="utf-8") as file_write:
        for el in list_names:
            file_write.write(f'{el[0]}\n')
            file_write.write(f'{el[1]}\n')
            with open(el[0], encoding="utf-8") as file_read:
                for i in file_read:
                    file_write.write(i)
                file_write.write('\n')


list_create()
merged_files(list_files)
with open('result.txt', encoding="utf-8") as f:
    print(f.read())
# =========case3 complete==========
