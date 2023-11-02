from pprint import pprint

#Задача №1 - данные из файла записываем в словарь
with open('recipes.txt', 'r', encoding='utf-8') as cook_f:
    cook_book = {}
    for line in cook_f:
        name_dish = line.strip()
        count = int(cook_f.readline().strip())
        dict_d = []
        for item in range(count):
            ingredient_name, quantity, measure = cook_f.readline().strip().split('|')
            dict_d.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[name_dish] = dict_d
        cook_f.readline()  # Пропускаем пустую строку

#Задача №2 - Нужно написать функцию, которая на вход принимает список блюд из cook_book
# и количество персон для кого мы будем готовить
def get_shop_list_by_dishes(dishes, person_count):
    grocery_dict = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_list = dict([(ingredient['ingredient_name'],
                                     {'quantity': int(ingredient['quantity']) * person_count,
                                      'measure': ingredient['measure']})])
            if grocery_dict.get(ingredient['ingredient_name']) == 'None':
                merger = (int(grocery_dict[ingredient['ingredient_name']]['quantity']) +
                           int(ingredient_list[ingredient['ingredient_name']]['quantity']))
                grocery_dict[ingredient['ingredient_name']]['quantity'] = merger
            else:
                grocery_dict.update(ingredient_list)
    return grocery_dict

# проверка работы функции
pprint(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 7))