from collections import defaultdict

def parse(filename):
    with open(filename, 'r') as fi:
        num_of_pizzas, T2, T3, T4 = map(int, fi.readline().split())

        pizzas = []
    
        pizzas_per_ingredient = defaultdict(list)
        for pizza in range(num_of_pizzas):
            line = fi.readline().split()
            num_of_ingredients = int(line[0])
            ingredients = line[1:]
            for i in ingredients:
                pizzas_per_ingredient[i].append(pizza)
            pizzas.append(set(ingredients))

        dataset = {
            'pizzas_per_ingredient': pizzas_per_ingredient,
            'unique_ingredients': set(pizzas_per_ingredient.keys()),
            'pizzas': pizzas,
            'T2': T2,
            'T3': T3,
            'T4': T4,
            'num_of_pizzas' : num_of_pizzas
        }
        return dataset