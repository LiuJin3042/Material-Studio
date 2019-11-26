import os


p = os.listdir()
p = [i for i in p if os.path.isdir(i) and i[0] != '.']
print(p)
for each_path in p:
    folder_path = './' + each_path  # ./构型1
    structure_files = os.listdir(folder_path)
    each_file_path = [folder_path + '/' + i for i in structure_files if i[-1] != 'z']
    for file in each_file_path:
        with open(file, 'r+') as f:
            f_list = f.readlines()
            f_list = ['Li ' + i for i in f_list]  # 在每一行添加原子名称
            f_list.insert(0, str(len(f_list)) + '\n\n')
        with open(file + '.xyz', 'w', encoding='utf8') as f:
            f.writelines(f_list)


