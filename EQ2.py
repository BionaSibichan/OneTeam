ages={"Priya":19,"Ravi":24,"Aman":27,"Neha":22,"Kiran":20}
yto = sorted(ages.items(),lambda x:x)
print([name for name, age in yto])
