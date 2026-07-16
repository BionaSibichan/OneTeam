def mix_pattern():
    l=int(input("Enter length:"))
    for i in range(1,l+1):
        print(" "*(l-i),end="")
        for j in range((2*i-1)):
            if (j%2==0):
                print("*",end="")
            else:
                print("#",end="")
        print()
mix_pattern()