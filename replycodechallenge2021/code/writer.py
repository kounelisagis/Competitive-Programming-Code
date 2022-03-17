def write(solution, filename):

    with open(filename, 'w') as fo:
        fo.write(str(len(solution))+'\n')
        for ANT1_id, coords in solution.items():
            fo.write( str(ANT1_id) + ' ' + str(coords[0]) + ' ' + str(coords[1]) + '\n')
