with open('example7.txt') as text:
    while True:
        dish = {}
        dishes = {}
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
        print(dish.fromkeys((a,), e))
        text.readline()
    
