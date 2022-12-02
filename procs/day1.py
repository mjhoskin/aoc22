import itertools as it
import pandas as pd

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

def proc_d1():
    day = 1
    path = get_path(day)

    with open(path) as f:
        d = [r.strip() for r in f.readlines()]

    splits = [list(sub) for ele, sub in it.groupby(d, key=bool) if ele]

    out = pd.DataFrame(splits)
    out = out.reset_index()
    out = pd.melt(out, id_vars='index', value_vars=out.columns[1:]).dropna()
    out = out.drop(columns=['variable'])
    out.to_csv(get_path(1, mode="proc"), index=False)

if __name__ == '__main__':
    proc_d1()