from json import load

f=open("C:\\Users\\user\\Desktop\\my python\\json_works\\students.json","r")

data= load(f)

print(data) 

# all_name=[emp.get("name") for emp in data]
# print(all_name)

all_dep={emp.get("department") for emp in data}
print(all_dep)

max_salary=max(data,key=lambda d:d.get("salary"))
print(max_salary)