def read_input(filename):

 input_file = open(filename, "r")
    line = input_file.readline()
    line = line.split()
    Si = int(line[0])
    Smax = int(line[1])
    T = int(line[2])
    D = int(line[3])
    demons = []
	
   
    for i in range(D):
        line = input_file.readline()
        line = line.split()
        demon = [int(line[0]), int(line[1]), int(line[2]), int(line[3]), [int(x) for x in line[4:]]]
        demons.append(demon)

    input_file.close()
    return Si, Smax, T, D, demons
