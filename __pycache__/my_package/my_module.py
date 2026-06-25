def is_even(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")

def is_prime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                print("Not Prime")
                break
        else:
            print("Prime")
    else:
        print("Not Prime")
