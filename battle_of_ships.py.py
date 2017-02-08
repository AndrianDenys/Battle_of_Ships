def read_file():
    """
    Converts file in list of lines and checks size of field
    >read_file()
    >> %lines%, True
    """
    temp = False
    i = 0
    with open("file.txt", "r") as f:
        lines = f.readlines()
        if len(lines) > 10:
            return temp
        else:
            while i < 10:
                if len(lines[i]) > 10:
                    return temp
                else:
                    i += 1
    return lines, temp

def has_ship(x, y):
    """
    Checks content of that coordinate. If there is normal or damaged ship - returns True.
    >has_ship(0, 0)
    >> False
    """
    temp = False
    lines = read_file()
    if lines[x][y] == "*" or lines[x][y] == "X":
        temp = True
    return temp


def ship_size(x, y):
    """
    Checks content of coordinate. If there is any ship, than returns its size.
    >ship_size(0,0)
    >>3
    """
    size = 0
    if has_ship(x, y):
        size += 1
        if has_ship(x-1, y):
            size += 1
            if has_ship(x - 2, y):
                size += 1
                if has_ship(x - 3, y):
                    size += 1
        elif has_ship(x+1, y):
            size += 1
            if has_ship(x+2, y):
                size += 1
                if has_ship(x+3, y):
                    size += 1
        elif has_ship(x, y-1):
            size += 1
            if has_ship(x, y-2):
                size += 1
                if has_ship(x, y-3):
                    size += 1
        elif has_ship(x, y+1):
            size += 1
            if has_ship(x, y+2):
                size += 1
                if has_ship(x, y+3):
                    size += 1
    return size


def is_valid():
    """
    Checks number of ships on the field
    >is_valid()
    >>True
    """
    temp = False
    i = 0
    j = 0
    cap_ship = 0 #size 4
    large_ship = 0 #size 3
    mid_ship = 0 #size 2
    small_ship = 0 #size 1
    while i < 11:
        while j < 11:
            if ship_size(i, j) == 4:
                cap_ship += 1
                j += 1
            elif ship_size(i, j) == 3:
                large_ship += 1
                j += 1
            elif ship_size(i, j) == 2:
                mid_ship += 1
                j += 1
            elif ship_size(i, j) == 1:
                small_ship += 1
                j += 1
        i += 1
        j = 0
    if (cap_ship == 4) and (large_ship == 6) and (mid_ship == 6) and (small_ship == 4):
        temp = True
    return temp

