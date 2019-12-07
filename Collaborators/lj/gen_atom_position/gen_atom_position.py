import os


def change_atom(contents, position):
    for i in position:
        contents[i+1] = contents[i+1].replace('Li', 'Mn')
    file_name = 'Li' + str(19-len(position)) + 'Mn' + str(len(position)) + '_'\
                    + ''.join([str(i) + '_' for i in position]).rstrip('_') + '.xyz'
    with open(file_name, 'w+') as f:
        f.writelines(contents)
    return 0


origin_file = './Li_159.xyz'


for atom_1 in range(1, 20):
    position = [atom_1]
    with open(origin_file, 'r+') as f:
        origin_contents = f.readlines()
    change_atom(origin_contents, position)
