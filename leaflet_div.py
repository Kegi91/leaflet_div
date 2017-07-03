import numpy as np

def get_num(x):
    return int(''.join(c for c in x if c.isdigit()))

def print_leaflet(fname, center):
    f = open(fname, 'r')
    next(f)
    next(f)

    line = f.readline()
    split = line.split()

    upper = []
    lower = []

    while line != '':
        if len(split) not in [5,6]: # TODO: Make universal
            line = f.readline()
            split = line.split()
            continue

        res = split[0]
        atom = split[1]
        z = float(split[-1]) # TODO: Make universal

        if res.find("DPPC") != -1 and atom.find("P") != -1: # TODO: Make universal
            if z < center:
                lower.append(get_num(res))
            else:
                upper.append(get_num(res))

        line = f.readline()
        split = line.split()

    f.close()

    print("\nUpper:\t%d-%d"%(upper[0],upper[-1]))
    print_consecutive_elems(upper)
    print("\nLower:\t%d-%d"%(lower[0],lower[-1]))
    print_consecutive_elems(lower)

def find_center(fname):
    f = open(fname, 'r')
    next(f)
    next(f)

    line = f.readline()
    split = line.split()

    upper = []
    lower = []

    z_sum = 0
    z_numb = 0

    while line != '':
        if len(split) not in [5,6]: # TODO
            line = f.readline()
            split = line.split()
            continue

        res = split[0]
        atom = split[1]
        z = float(split[-1]) # TODO

        if res.find("DPPC") != -1 and atom.find("P") != -1: # TODO
            z_sum += z
            z_numb += 1

        line = f.readline()
        split = line.split()

    f.close()
    return z_sum/z_numb

def print_consecutive_elems(array):
    prev = array[0]
    low = array[0]
    for i in range(1,len(array)):
        if array[i] == prev + 1:
            prev = array[i]
            continue
        else:
            print("%d-%d"%(low, array[i-1]))
            low = array[i]
            prev = array[i]

    print("%d-%d\n"%(low, array[i]))

print_leaflet(
    "input/system_solv.gro",
    find_center("input/system_solv.gro")
)
