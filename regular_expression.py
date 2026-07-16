import re
l="what coconut 77coco"
#n=re.search("coco",l)
n=re.findall("coco",l)
# print(n)
# print(n.start())
# print(n.end())
n=re.findall(r'\d',l)
print(n)
