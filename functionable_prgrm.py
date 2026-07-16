numbers=[2,5,7,9]
# n=list(map(lambda num:num*2,numbers))#auto iterate and return boolean val
# n=list(filter(lambda num:num%2==0,numbers))#return T&F numb
# print(n)

from functools import reduce
#total=reduce(lambda x,y:x+y,numbers)
fact=reduce(lambda x,y:x*y,range(1,5))
print(fact)
