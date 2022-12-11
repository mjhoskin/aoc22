# day 7
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


def proc_d8():
    day = "8_sub"
    path = get_path(day)

    with open(path) as f:
        d = [list(i) for i in f.read().split('\n')]

    cell_info = []
    for row_idx, row in enumerate(d):
        cell_info.append(["STARTt", f"0_{row_idx}", f"{row_idx}_0", -1])
        for col_idx, height_str in enumerate(row):
            below = f"{row_idx+1}"
            right = f"{col_idx+1}"
            if below == str(len(d)):
                below = "STARTt"
            else:
                below = f"{below}_{col_idx}"
            if right == str(len(row)):
                right = "STARTt"
            else:
                right = f"{row_idx}_{right}"

            cell_info.append([f"{row_idx}_{col_idx}",
                              f"{below}",
                              f"{right}",
                              height_str])

    with open(get_path("8-4", "test"), 'w') as f:
        f.write("node vert hzt height\n")
        for row in cell_info:
            f.write(f"t{row[0]} t{row[1]} t{row[2]} {row[3]}\n")


if __name__ == '__main__':
    proc_d8()
