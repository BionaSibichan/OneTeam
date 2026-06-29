class Students:
    institute="OneTeam"

    # def get_details(self,name,place):
    #     self.name=name
    #     self.place=place
    def __init__(self,name,place):
        self.name=name
        self.place=place

    def display(self):
        print(self.name,"from" ,self.place,"studying in",self.institute)
std1=Students("Anas","Oman")
# std2=Students()
# std3=Students()

# std1.get_details("Anas","Oman")
# std2.get_details("Charls","Kottayam")
# std3.get_details("Richard","Kottayam")

std1.display()
# std2.display()
# std3.display()