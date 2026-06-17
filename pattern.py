# for r in range(5):
#     for j in range(r+1):
#         print("*",end=" ")
#     print("")   OR

for r in range(1,6):
    print("* "*r)

# for r in range(1,6):
#     print("*"(6-r)*r)
        
# Right-aligned star pattern

for r in range(1, 6):
    print(" " * (6 - r) + "*" * r)
