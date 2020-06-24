def make_dict():
    with open('example7.txt') as text:
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
##        print(dishes_dict )
    return dishes_dict


##def get_shop_list_by_dishes(dishes, person_count):
person_count = int(input('Введите количество гостей'))
dishes = input( 'Введите блюда через запятую' ).split(', ')
##print(dishes)

k = []
l = ['measure', 'quantity']

n = {}
o = {}
for i in dishes:
    if i in make_dict().keys():
       for j in make_dict().get(i):
           m = []
           k.append(j.get('ingredient_name'))
           m = (j.get('measure'), j.get('quantity') * person_count)
           n = dict(zip(l, m))
print(o.fromkeys(k, n))

           
           
           
               
       



















    
##{'Омлет': [{'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
##           {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
##           {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}],
## 'Утка по-пекински': [{'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
##                      {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
##                      {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
##                      {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}],
## 'Запеченный картофель': [{'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
##                          {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
##                          {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'}],
## 'Фахитос': [{'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'г'},
##             {'ingredient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт'},
##             {'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
##             {'ingredient_name': 'Винный уксус', 'quantity': 1, 'measure': 'ст.л'},
##             {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}]}  
##  



            
     
       

  
