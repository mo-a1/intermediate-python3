import filecmp

# ###################### function: filecmp.cmp() ######################### #
print(filecmp.cmp("testes/linecash.txt", "testes/linecash_copy.txt"))

path1 = r"C:\Users\20106\PycharmProjects\intermediate-python3\Files and Paths Modules\testes\test_1"
path2 = r"C:\Users\20106\PycharmProjects\intermediate-python3\Files and Paths Modules\testes\test_1_copy"

# ###################### class: filecmp.dircmp() ######################### #

# attributes and methods
# [ 'common', 'common_dirs', 'common_files', 'common_funny', 'hide', 'ignore', 'left', 'left_list', 'left_only',
# 'methodmap', 'report', 'report_full_closure', 'report_partial_closure', 'right', 'right_list', 'right_only']

dir_comp = filecmp.dircmp(path1, path2)
print(dir_comp.common_files)
print(dir(dir_comp))
