from collections import defaultdict
from collections import deque  

def parse(filename):
    dataset = {}

    with open(filename, 'r') as fi:

        duration, num_of_intersections, num_of_streets, num_of_cars, F = map(int, fi.readline().split())

        intersections = {}
        streets = {}
        for _ in range(num_of_streets):
            line = fi.readline().split()
            start_inter = int(line[0])
            end_inter = int(line[1])
            street_name = line[2]
            L = int(line[3])
            if start_inter not in intersections:
                intersections[start_inter] = {}
            intersections[start_inter][end_inter] = {}
            intersections[start_inter][end_inter]['name'] = street_name
            intersections[start_inter][end_inter]['L'] = L
            streets[street_name] = (start_inter, end_inter, L)


        car_paths = []
        for _ in range(num_of_cars):
            line = fi.readline().split()

            path_streets = line[1:]
            car_paths.append(path_streets)


        dataset = {
            "duration" : duration,
            "num_of_intersections": num_of_intersections,
            "num_of_streets": num_of_streets,
            "num_of_cars": num_of_cars,
            "F": F,
            "intersections": intersections,
            "streets": streets,
            "car_paths": car_paths
        }


    return dataset


