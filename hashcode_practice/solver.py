import random


def solve(dataset):

    num_of_teams_that_got_their_pizza_today = 0
    # each team X members -> no pizza, X pizzas
    ingred_to_pizzas, pizzas, T2,T3,T4 = dataset['pizzas_per_ingredient'], dataset["pizzas"], dataset['T2'], dataset['T3'], dataset['T4']
    pizzas_each = []


    def get_greedy_pizza(max_iterations, all_ingredients, curr_ingredients):
        """max iter > 1"""
        if max_iterations == 0:
            return None
        def find_best_pizza(max_pizzas, chosen_ingred):
            best_so_far = i = 0
            curr_num_of_diff = []
            while i < max_pizzas and i < len(ingred_to_pizzas[chosen_ingred]):
                curr_pizza = ingred_to_pizzas[chosen_ingred][i]
                if len(pizzas[curr_pizza] - curr_ingredients) > best_so_far:
                    best_so_far = len(pizzas[curr_pizza] - curr_ingredients)
                    final_pizza = curr_pizza
                i+=1
            return final_pizza
        
        result = None
        ingredients_left = all_ingredients - curr_ingredients
        if len(ingredients_left) == 0:
            return None

        chosen_ingred = random.sample(ingredients_left,1)[0]
        curr_pizza = find_best_pizza(10, chosen_ingred)

        
        while curr_pizza not in valid_pizza_ids and max_iterations > 0:
            chosen_ingred = random.sample(ingredients_left,1)[0]
            curr_pizza = find_best_pizza(10, chosen_ingred)
            max_iterations -= 1

        if max_iterations > 0: result = curr_pizza
        return result


    # 1. select random pizza (P0)
    # 2. set(ingredients) 


    T = [T2, T3, T4]
    teams_sizes = [2,3,4]


    teams_left = T2+T3+T4
    valid_pizza_ids = set(range(len(pizzas)))

    
    while teams_left>0 and len(valid_pizza_ids) >= min([i+2 for i in T if i != 0]):
        # get random team
        team_size = random.choice(teams_sizes)
        if T[team_size-2] == 0:
            continue
        

        curr_ingredients = set()
        curr_pizzas = []
        MAX_ITER = 100

        if len(valid_pizza_ids) - team_size >= 0:
            while len(curr_pizzas) < team_size:
                curr_pizza = get_greedy_pizza(MAX_ITER, dataset['unique_ingredients'],  curr_ingredients)
                if not curr_pizza: 
                    curr_pizza = random.sample(valid_pizza_ids,1)[0] # M*N
                valid_pizza_ids.remove(curr_pizza)
                [curr_ingredients.add(ingr) for ingr in pizzas[curr_pizza]]
                curr_pizzas.append(curr_pizza)


            assert len(curr_pizzas) == team_size

            num_of_teams_that_got_their_pizza_today += 1
            T[team_size-2] -= 1
            orders = [team_size] + curr_pizzas
            pizzas_each.append(orders)

            teams_left -= 1


    solution = {
        "number_of_teams_delivered" : num_of_teams_that_got_their_pizza_today,
        "pizzas_each" : pizzas_each
    }

    return solution

