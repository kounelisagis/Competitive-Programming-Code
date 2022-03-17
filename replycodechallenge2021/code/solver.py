import random
import random
import math
from statistics import mean
from sklearn.cluster import KMeans
import numpy as np

def solve(dataset):

    # 1. FOR EACH ANT1, PLACE ON BOARD
    # 2. KEEP TRACK OF LOCATIONS
    # 3. GET SCORE
    # 4. RANDOM REPLACE, CHECK IF SCORE BETTER

    solution = dict() #key: (x,y), value: ATN1_id3.
    locations_used = set()

    ANT1as = [ l + [id] for id, l in enumerate(dataset['ANT1as']) ]
    ANT1as = sorted(ANT1as, key=lambda x: x[1], reverse=True)
    buildings = sorted(dataset['buildings'], key=lambda x: x[3], reverse=True)
    avg_BL = mean(value[3] for value in buildings)

    for i in range(len(ANT1as)):
        ANT1id = ANT1as[i][-1]
        xb, yb, BL = buildings[i][0], buildings[i][1], buildings[i][2]
        # 0 < |xb - xa| + |yb - ya| < AR
        AR = ANT1as[i][0]

        r = math.floor(AR/2)
        if BL > avg_BL:
            r = math.floor( (AR/2)/math.exp(BL/avg_BL) )

        xa = random.randint( max(xb - r, 0), min(xb + r, dataset['Width'] - 1) )
        ya = random.randint( max(yb - r, 0), min(yb + r, dataset['Height'] - 1) )

        iterations = 1000
        while((xa, ya) in locations_used) and iterations > 0:
            xa = random.randint( max(xb - r, 0), min(xb + r, dataset['Width'] - 1) )
            ya = random.randint( max(yb - r, 0), min(yb + r, dataset['Height'] - 1) )
            iterations -= 1

        if iterations == 0:
            xa = random.randint(0,dataset['Width']-1)
            ya = random.randint(0,dataset['Height']-1)

            iterations = 1000
            while((xa, ya) in locations_used) and iterations > 0:
                xa = random.randint(0,dataset['Width']-1)
                ya = random.randint(0,dataset['Height']-1)
                iterations -= 1

            if iterations == 0:
                continue

        locations_used.add( (xa, ya) )
        solution[ANT1id] = (xa, ya)

    return solution
