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

make_dict()

##def get_shop_list_by_dishes(dishes, person_count):
person_count = int(input('Введите количество гостей'))
dishes = input( 'Введите блюда через запятую' ).split(', ')
##print(dishes)

k = []
kk = []
l = ['measure', 'quantity']
p = []
n = {}
o = {}
t = {}
s = {}
for dish in dishes:

    if dish in make_dict().keys():
        for ingredient in make_dict().get(dish):
##            print(ingredient)
            m = []
            k = ingredient.get('ingredient_name')
##            print('k:', k)
            kk.append(k)
##            print('kk:', kk)
            m = (ingredient.get('measure'), ingredient.get('quantity') * person_count)
##            print('m:', m)
            n = dict(zip(l,m))
##            print('n:', n)
            if kk.count(k) == 1:
                print('kk_count:', kk.count(k))
                t.update(o.fromkeys((k,), n))
    
            else:
                print('kk_count:', kk.count(k))
##                (t.pop(k).get('quantity'))     уже умножено на число гостей
                print(ingredient.get('quantity'))
##              
                m = (ingredient.get('measure'), ingredient.get('quantity')*person_count + (t.pop(k).get('quantity')))
                print('m:', m)
                
                n = dict(zip(l,m))
                t.update(o.fromkeys((k,), n))
print('t:', t)
   

  
