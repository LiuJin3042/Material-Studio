import os


def change_atom(origin_file, contents, position):
    for i in position:
        contents[i+1] = contents[i+1].replace('Li', 'Mn')
    file_name = 'Li' + str(19-len(position)) + 'Mn' + str(len(position)) + '_'\
                    + ''.join([str(i) + '_' for i in position]).rstrip('_') + '.xyz'
    new_folder = origin_file.rstrip('.xyz') + '_' + str(len(position))
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    with open(new_folder + '/' + file_name, 'w+') as f:
        f.writelines(contents)
    return 0


origin_file = './Li_025.xyz'


for atom_1 in range(1, 20):
    for atom_2 in range(atom_1+1, 20):
        for atom_3 in range(atom_2+1, 20):
            position = [atom_1, atom_2, atom_3]
            with open(origin_file, 'r+') as f:
                origin_contents = f.readlines()
            change_atom(origin_file, origin_contents, position)
