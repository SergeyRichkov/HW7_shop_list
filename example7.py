def make_dict():
    with open('recipes.txt') as text:
        dish = {}
        dishes_dict = {}
        while True:
            e = []
            a = text.readline().rstrip()
            if not a:
                break
            b = int(text.readline().rstrip())
            c = ['ingredient_name', 'quantity', 'measure']
            for i in range(b):
                d = text.readline().rstrip().split(' | ')
                for f in d:
                    d[1] = int(d[1])
                e.append(dict(zip(c, d)))
                dishes_dict.update(dish.fromkeys((a,), e))
            text.readline()
    return dishes_dict

make_dict()

def get_shop_list_by_dishes(dishes, person_count):

    
##person_count = int(input('Введите количество гостей'))
##dishes = input( 'Введите блюда через запятую' ).split(', ')

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
get_shop_list_by_dishes(['Омлет', 'Салат'], 2)

   

  
