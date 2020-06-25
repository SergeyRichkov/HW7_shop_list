def make_dict():
    with open('recipes.txt') as text:
        dish = {}
        dishes_dict = {}
        while True:
            recipe = []
            dish_name = text.readline().rstrip()
            if not dish_name:
                break
            amount_of_ingredients = int(text.readline().rstrip())
            dishes_keys = ['ingredient_name', 'quantity', 'measure']
            for i in range(amount_of_ingredients):
                each_ingredient_list = text.readline().rstrip().split(' | ')
                for element in each_ingredient_list:
                    each_ingredient_list[1] = int(each_ingredient_list[1])
                recipe.append(dict(zip(dishes_keys, each_ingredient_list)))
                dishes_dict.update(dish.fromkeys((dish_name,), recipe))
            text.readline()
    return dishes_dict

def get_shop_list_by_dishes(dishes, person_count):  
    units = ['measure', 'quantity']
    current_ingredient = 0
    ingredients_list = []
    how_much_units = {}
    one_ingredient_dict = {}
    shop_dict = {}
    for dish in dishes:
        if dish in make_dict().keys():
            for ingredient in make_dict().get(dish):
                ingredients_for_all_person = []
                current_ingredient = ingredient.get('ingredient_name')
                ingredients_list.append(current_ingredient)
                ingredients_for_all_person = (ingredient.get('measure'),
                ingredient.get('quantity') * person_count)
                how_much_units = dict(zip(units, ingredients_for_all_person))
                        
                if ingredients_list.count(current_ingredient) == 1:
                    shop_dict.update(one_ingredient_dict.fromkeys(
                (   current_ingredient,), how_much_units))
                
                else:
                    ingredients_for_all_person = (ingredient.get('measure'),
                    ingredient.get('quantity')*person_count +
                    (shop_dict.pop(current_ingredient).get('quantity')))
                
                    how_much_units = dict(zip(units, ingredients_for_all_person))
                    shop_dict.update(one_ingredient_dict.fromkeys(
                    (current_ingredient,), how_much_units))
    print(shop_dict)
    return
get_shop_list_by_dishes(['Омлет', 'Салат', 'Фахитос'], 2)

  
