#day 6

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


def proc_d6():
    day = 6
    path = get_path(day)

    with open(path) as f:
        with open(get_path(day, mode='proc'), "w") as f_out:
            for i, char in enumerate(f.readline()):
                f_out.write(f"{i+1} {i+2} {char}\n")


if __name__ == '__main__':
    proc_d6()
