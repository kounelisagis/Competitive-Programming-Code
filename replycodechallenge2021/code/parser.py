from collections import defaultdict

def parse(filename):
    with open(filename, 'r') as fi:
        W, H = map(int, fi.readline().split())
        N, M, R = map(int, fi.readline().split())
        
        buildings = []
        for _ in range(N):
            X, Y, L, C = map(int, fi.readline().split())
            buildings.append([X, Y, L, C])

        antennas = []
        for _ in range(M):
            R,C = map(int, fi.readline().split())
            antennas.append([R,C])


        dataset = {
            'Width': W,
            'Height': H,
            'Num_buildings': N,
            'Num_ANT1': M,
            'Reward': R,
            'buildings': buildings,
            'ANT1as' : antennas
        }
        return dataset
