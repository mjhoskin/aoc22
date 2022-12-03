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

def proc_d3():
    day = 3
    path = get_path(day)

    d = []
    with open(path) as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            length = int(len(line)/2)

            initial_string = '\n{i} {i}_1 '.format(i=i).join(line[:length])
            second_string = '\n{i} {i}_2 '.format(i=i).join(line[length:])
            d.append(f"{i} {i}_1 {initial_string}\n{i} {i}_2 "
                     f"{second_string}\n")
    with open(get_path(day, mode='proc'), "w") as f_out:
        f_out.writelines(d)


def write_mapper_txt():

    for i in string.ascii_lowercase:
        print(f'  @@priority += ("{i}" -> {ord(i)-96});')
    for i in string.ascii_uppercase:
        print(f'  @@priority += ("{i}" -> {ord(i)-38});')


if __name__ == '__main__':
    proc_d3()