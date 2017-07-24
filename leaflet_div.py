import numpy as np

def skip_lines(f, i):
    for i in range(i):
        next(f)

def read_gro_line(f_in):
    l = f_in.readline()
    if l == '' or len(l)<45:
        return ''

    # a_number = int(l[15:20])
    # x = float(l[20:28])
    # y = float(l[28:36])

    res_name = l[5:10].strip()
    res_num = int(l[0:5])
    a_name = l[10:15].strip()
    z = float(l[36:44])

    return res_name, res_num, a_name, z

def print_leaflet(fname, res_name, atom_name):
    f = open(fname, 'r')
    skip_lines(f,2)

    upper = []
    lower = []
    center = find_center(fname, res_name, atom_name)

    while True:
        try:
            res, res_num, atom, z = read_gro_line(f)
        except ValueError:
            break

        if res == res_name and atom == atom_name:
            if z < center:
                lower.append(res_num)
            else:
                upper.append(res_num)

    f.close()

    print("\nUpper leaflet (%d residues):\n"%(len(upper)))
    print_consecutive_elems(upper)
    print("\nLower leaflet (%d residues):\n"%(len(lower)))
    print_consecutive_elems(lower)

    print("\nCenter at z = %.3f\n"%(center))

def find_center(fname, res_name, atom_name):
    f = open(fname, 'r')
    skip_lines(f,2)

    z_sum = 0
    z_numb = 0

    while True:
        try:
            res, res_num, atom, z = read_gro_line(f)
        except ValueError:
            break

        if res == res_name and atom == atom_name:
            z_sum += z
            z_numb += 1

    f.close()

    try:
        return z_sum/z_numb
    except ZeroDivisionError:
        print("\nNo matches found. Check res_name and atom_name.\n")
        raise

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

if __name__ == "__main__":
    print_leaflet(
        "input/system_solv.gro",
        "DPPC",
        "P8"
    )
