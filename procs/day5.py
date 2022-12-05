import re

def get_path(day, mode="real"):

    if mode=="test":
        path = f"test_data/d{day}.txt"
    elif mode=="proc_top":
        path = f"out_data/d{day}_stack.txt"
    elif mode=="proc_bot":
        path = f"out_data/d{day}_cmds.txt"
    elif mode =="real":
        path = f"data/d{day}.txt"
    else:
        path = f"data/d{day}.txt"

    return path

def get_stacks(input):
    stacks = input
    stack_count = len(stacks[-1].split())

    stack_loc_index = []
    for idx, stack in enumerate(stacks[-1]):
        if stack != " ":
            stack_loc_index.append(idx)

    height = len(stacks) - 2

    tidy_stacks = [[] for _ in range(stack_count)]
    for level in range(height, -1, -1):
        fill_stack = stacks[level]

        for stack_idx, loc_idx in enumerate(stack_loc_index):
            if len(fill_stack) > loc_idx:
                if fill_stack[loc_idx] != ' ':
                    tidy_stacks[stack_idx] += fill_stack[loc_idx]

    return tidy_stacks

def proc_d5():
    day = 5
    path = get_path(day)

    with open(path) as f:
        full_input = f.read().split('\n\n')

    tidy_stacks = get_stacks(full_input[0].split('\n'))
    writable_stacks = ""
    for idx, stack in enumerate(tidy_stacks):
        writable_stacks += f"{idx+1} {''.join(stack)}\n"

    with open(get_path(day, mode='proc_top'), "w") as f_out:
        f_out.writelines(writable_stacks)

    cmds = []
    for cmd_row in full_input[1].split('\n'):
        cmds.append(re.findall(r'\d+', cmd_row))

    writable_cmds = ''
    for idx, stack in enumerate(cmds):
        writable_cmds += f"{idx} {' '.join(stack)}\n"

    with open(get_path(day, mode='proc_bot'), 'w') as f_out:
        f_out.writelines(writable_cmds)


if __name__ == '__main__':
    proc_d5()