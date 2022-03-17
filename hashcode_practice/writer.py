def write(solution, filename):

    with open(filename, 'w') as fo:
        fo.write(str(solution['number_of_teams_delivered'])+'\n')
        for team in solution['pizzas_each']:
            fo.write(" ".join(map(str,team))+'\n')
