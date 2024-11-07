import os

path = "C:\\Users\\gololobov\\Downloads\\P33\\"
# dir1 = "Test"

def spy(path):
    path = os.path.normpath(path)
    result = {"dirs":[], "files":[]}
    for path, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            result["dirs"].append(dir)
        for file in filenames:
            result["files"].append(file)
    with open("spy.txt", "w") as f:
        f.write("\n{:-^30}\n".format("DIRECTORIES"))
        for dir in result["dirs"]:
            f.write("[" + dir + "]\n")
        f.write("\n{:-^30}\n".format("FILES"))
        for file in result["files"]:
            f.write(f"{file}\n")


#spy(path)



# path = os.path.join(path, dir1)
# os.mkdir(path)

# print(os.path.isdir(path))
# print(os.path.isabs(path))
# print(os.path.isfile(path))
# print(os.path.islink(path))

# f = open("text.txt", "w")
# f.write("Hello Python")
# f.close()

f = open("text.txt", "r")
list_ = f.readlines()
f.close()
for i in range(len(list_)):
    list_[i] = list_[i].replace('\n', '')
print(list_)

#
# with open("text.txt", "r") as f:
#     print(f.readlines())
#
# print(os.path.getsize(path))
# print(os.path.getmtime(path))
# print(os.path.getatime(path))
# print(os.path.getctime(path))

# print(path)
#
# for path, dirnames, filenames in os.walk(path):
#     print(path)
#     print(dirnames)
#     print(filenames)