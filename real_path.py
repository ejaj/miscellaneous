import os
print("Current File Name : ",os.path.realpath(__file__))

path = "/"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# print the list
print(dir_list)