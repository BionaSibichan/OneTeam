# file=open("sample.txt","w")
# file.write("wow fantastic")
# file.close()

# with open("sample.txt","w") as file:
#     file.write("elastic and plastic with block")


filename = "student.txt"

try:
    file = open(filename, "x")
    print("File created")
    file.close()
except FileExistsError:
    print("File already exists")

file = open(filename, "w")
file.write("Name: Rahul\n")
file.write("Age: 20\n")
file.write("Course: BCA\n")
file.close()

file = open(filename, "r")
print("Complete File")
print(file.read())
file.close()

file = open(filename, "r")
print("First 10 Characters")
print(file.read(10))
file.close()

file = open(filename, "r")
print("First Line")
print(file.readline())
print("Second Line")
print(file.readline())
file.close()

file = open(filename, "r")
print("All Lines")
print(file.readlines())
file.close()

file = open(filename, "a")
file.write("College: XYZ College\n")
file.close()

file = open(filename, "r+")
print("r+ Mode")
print(file.read())
file.write("City: Kochi\n")
file.close()

file = open(filename, "w+")
file.write("Python File Handling\n")
file.write("Easy Example\n")
file.seek(0)
print("w+ Mode")
print(file.read())
file.close()

file = open(filename, "a+")
file.write("Learning Python\n")
file.seek(0)
print("a+ Mode")
print(file.read())
file.close()

file = open(filename, "r")
print("Current Position:", file.tell())
print(file.read(6))
print("Position After Reading:", file.tell())
file.seek(0)
print(file.read())
file.close()

with open(filename, "r") as file:
    print("Using with")
    print(file.read())

