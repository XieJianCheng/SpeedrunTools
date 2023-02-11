# coding: utf-8
import os
import shutil

with open('delete_options.txt', 'r', encoding='utf-8') as fo_r:
    read = fo_r.readlines()

inst_path = read[0].strip()
inst_names_tmp = read[1:]
inst_names = []
for i in inst_names_tmp:
    inst_names.append(i.strip())
print(inst_path)
print(inst_names)

save_dirs = []
walk = os.walk(inst_path)
times = 0
for i in walk:
    if times >= len(inst_names):
        break
    # print(i[0].split('\\')[-1])
    if i[0].split('\\')[-1] in inst_names:
        times += 1
        save_dirs.append(f'{i[0]}\\.minecraft\\saves')
        # print('d1', i[0])

speedrun_worlds = []
for each_inst in save_dirs:
    walk_inst = os.walk(each_inst)
    for j in walk_inst:
        if len(j[0].split('\\')[len(inst_path.split('\\'))+3:]) == 1:
            # print('d2', j[0])
            world_name = j[0].split('\\')[-1]
            # print('d3', world_name)
            split_world_name = world_name.split(' ')
            if len(split_world_name) > 1:
                if split_world_name[1] == 'Speedrun':
                    speedrun_worlds.append(j[0])
for k in speedrun_worlds:
    print('deleting', k)
    shutil.rmtree(k)
