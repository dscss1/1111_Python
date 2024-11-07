name = "hello Serg, hello Python"
print("Hello Serg,\rHello Python")
print(name[-1])
print(name.capitalize())
print(name.title())
print(name.count("hello"))
print(name.endswith("Pythob"))
print(name.startswith("H"))
print(name.find("h"))
print(name.rfind("h"))
print("d234ert3/.45ert".isalnum())
print("mama".ljust(50), "papa")
print("mama".rjust(50), "papa")
print(name.split("o"))
d = 5
m = 11
y = 2024
print(f"{str(d).zfill(5)}.{m}.{y}")

import string

print(string.ascii_letters)

name1 = "1"
print(f"Роунд №{name1:#^25}", 1234)
f1 = 131/19
print(f"{f1:10.2f}")
p = 0.25345
print(f"{p:5.2%}")