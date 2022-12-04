import string

def get_path(day, mode="real"):

    if mode=="test":
        path = f"test_data/d{day}.txt"
    elif mode=="proc":
        path = f"out_data/d{day}.txt"
    elif mode =="real":
        path = f"data/d{day}.txt"
    else:
        path = f"data/d{day}.txt"

    return path

def proc_d4():
    day = 4
    path = get_path(day)

    d = []
    with open(path) as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            line_parts = [l.split('-') for l in line.split(',')]

            for l in line_parts:
                d.append(f"{i} {l[0]} {l[1]}\n")
    with open(get_path(day, mode='proc'), "w") as f_out:
        f_out.writelines(d)

# 1 2 4 5

if __name__ == '__main__':
    proc_d4()