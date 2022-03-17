def write(solution, filename):


    with open(filename, 'w') as fo:
        fo.write(str(solution["num_of_intersections"])+'\n') # a single integer A (0 ≤ A ≤ I ), the number of intersections for which you specify the schedule.
        for intersection_id in (solution["schedules"]): # for each intersection
            fo.write(str(intersection_id)+'\n') # a single integer i (0 ≤ i < I ) – the ID of the intersection
            fo.write(str(len(solution["schedules"][intersection_id]))+'\n') #a single integer E i (0 < E i) – the number of incoming streets 
            for streets in range(len(solution["schedules"][intersection_id])): #for each street
                fo.write("".join(str(solution["schedules"][intersection_id][streets][0])+' ')) # the street name
                fo.write("".join(str(solution["schedules"][intersection_id][streets][1])+'\n')) # an integer T (1 ≤ T ≤ D ) – for how long each street will have a green light

