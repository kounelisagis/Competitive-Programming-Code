def score(solution, dataset):


    total_score = 0

    for team in solution['pizzas_each']:
        uniques = set()
        team_score = 0

        for pizza_id in team[1:]:
            for ingredient in dataset['pizzas'][pizza_id]:
                if ingredient not in uniques:
                    uniques.add(ingredient)
                    team_score += 1

        total_score += team_score**2

    return total_score
