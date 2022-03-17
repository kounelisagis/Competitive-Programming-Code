import random
from collections import defaultdict

car_finish = []



def solve(dataset):
    D, streets, graph, paths = dataset["duration"], dataset["streets"], dataset["intersections"], dataset["car_paths"]
    
    counter = defaultdict(lambda: defaultdict(int))
    for car_path in paths:
        for street in car_path:
            intersection = streets[street][1]
            counter[intersection][street] += 1

    inter_to_streets = defaultdict(list)
    for intersection in counter:
        max_streat = None
        max_num = -1
        for street in counter[intersection]:
            if not max_streat or counter[intersection][street] > max_num:
                max_num = counter[intersection][street]
                max_streat = street
                inter_to_streets[intersection].append(max_streat)


    schedules = {key: [[value[i],i**2+1] for i in range(len(value))] for key, value in inter_to_streets.items()}


    solution = {
        "num_of_intersections": len(schedules),
        "schedules": schedules
    }
    return solution
