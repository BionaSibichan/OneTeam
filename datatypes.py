string="hahaha"
print(type(string))
list=[7,5,"woww",[6,9],14]
print(type(list))
list[3]="hihi"
print(list)
tuple=(7,3,12.3,"ded")
print(type(tuple))
t=(7)              #this is not a tuple, this is an integer
print(type(t))
t=(7,)             #this is a tuple, because of the comma
print(type(t))
g=set([7,5,3,7,2,1]) #creating a set from a list
print(type(g))
    
set={7,5,3,7,2,1}
print(type(set))
print(set)
dict={"name":"Anzo","age":25,"city":"Oman","hobbies":["coding","gaming","traveling"]}
print(type(dict))
dict["age"]=26
print(dict)