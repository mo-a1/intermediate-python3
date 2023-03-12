import filecmp

# ###################### function: filecmp.cmp() ######################### #
print(filecmp.cmp("testes/linecash.txt", "testes/linecash_copy.txt"))

path1 = r"D:\Programing\Learning\Code\python3\intermediate-python3\Python Standard Library\File and Directory Access\testes\test_1"
path2 = r"D:\Programing\Learning\Code\python3\intermediate-python3\Python Standard Library\File and Directory Access\testes\test_1_copy"

# ###################### class: filecmp.dircmp() ######################### #

# attributes and methods
# [ 'common', 'common_dirs', 'common_files', 'common_funny', 'hide', 'ignore', 'left', 'left_list', 'left_only',
# 'methodmap', 'report', 'report_full_closure', 'report_partial_closure', 'right', 'right_list', 'right_only']

dir_comp = filecmp.dircmp(path1, path2)
print(dir_comp.common_files)
print(dir_comp)
print(dir(dir_comp))
