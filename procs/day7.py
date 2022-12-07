#day 7
import os
from collections import defaultdict
import pandas as pd

def get_path(day, mode="real"):
    if mode == "test":
        path = f"test_data/d{day}.txt"
    elif mode == "proc":
        path = f"out_data/d{day}.txt"
    elif mode == "real":
        path = f"data/d{day}.txt"
    else:
        path = f"data/d{day}.txt"

    return path


def is_file(line):
    ret_value = False
    if line[0].isdigit():
        ret_value = True

    return ret_value


def is_dir(line):
    ret_value = False
    if line[:3] == "dir":
        ret_value = True

    return ret_value


def is_cd(line):
    ret_value = False
    if line[:4] == "$ cd":
        ret_value = True

    return ret_value

def proc_d7():
    day = 7
    path = get_path(day)

    with open(path) as f:
        d = f.read().split('\n')

    path = '/'

    contents = defaultdict(list)
    instr = []
    for row in d:
        if is_cd(row):
            if row.split()[2] == "..":
                path = os.path.split(path)[0]
            else:
                temp_instr = []
                temp_instr.append(path)
                path = os.path.join(path, row.split()[2])
                temp_instr.append(path)

                instr.append(temp_instr)

        elif is_dir(row):
            l = (row.split()[0])

            contents[path] += [row.split()[1]]

        elif is_file(row):
            # print(row.split()[1])
            # print(row.split()[0])
            contents[path].append((row.split()[1], row.split()[0]))
            temp_instr = []
            temp_instr.append(path)
            temp_instr.append('')
            temp_instr.append(os.path.join(path,row.split()[1]))
            temp_instr.append(row.split()[0])

            instr.append(temp_instr)

    df = pd.DataFrame(instr, columns=['container', 'dir_content','file_content',
                                      'file_size'])

    df = df[df['dir_content'] != df['container']]
    df = df.replace('', None)
    df.to_csv(get_path(7, 'proc'), index=False)

if __name__ == '__main__':
    proc_d7()
