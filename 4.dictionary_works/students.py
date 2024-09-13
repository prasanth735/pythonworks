


students=[
    {"id":1,"name":"jhon","skills":["c","c++"],"exp":2,"qualification":"mca"},
    {"id":1,"name":"jain","skills":["python","js"],"exp":0,"qualification":"btec"},
    {"id":1,"name":"vijin","skills":["c","java","python"],"exp":4,"qualification":"mca"},
    {"id":1,"name":"tinu","skills":["r","java"],"exp":3,"qualification":"mtech"},
    {"id":1,"name":"roy","skills":["python","css","js"],"exp":0,"qualification":"bca"},
    {"id":1,"name":"vijil","skills":["js","r","css"],"exp":1,"qualification":"mtech"},
    {"id":1,"name":"ravi","skills":["java","python"],"exp":3,"qualification":"btec"},
    {"id":1,"name":"tom","skills":["java","css","r","sql"],"exp":4,"qualification":"bca"},
    {"id":1,"name":"ryan","skills":["c","css","python"],"exp":0,"qualification":"mca"},
   
    
]

#q1 total students

print(" toatal number of studen is", len(students))

#q2 print all students name

for stud in students:
    print(stud.get("name"))

all_students_name=[stud.get("name") for stud in students]
print(all_students_name)


#q3 students with exp >1
all_students_name=[stud.get("name") for stud in students if stud.get("exp")>1]
print(all_students_name)


#q4 students with skill java and python

for stud in students:
    if "java" in stud.get("skills") and "python" in stud.get("skills"):
        print(stud.get("name"))


# mca qualification students

for stud in students:
    if stud.get("qualification")=="mca":
        print(stud.get("name"))


# most exp student

most_exp_std=max(students,key= lambda std:std.get("exp"))
highest_exp=most_exp_std.get("exp")

exp_stud=[stud.get("name") for stud in students if stud.get("exp")==highest_exp]
print(exp_stud)


# students with > 2 skills

for stud in students:
    if len(stud.get("skills"))>2:
        print(stud.get("name"))


# students name starts with j

for stud in students:
    if stud.get("name").startswith("j"):
        print(stud.get("name"))
    


#  skill count

skill_count={}

for stud in students:
    skill=stud.get("skills")
    for sk in skill:
        if sk in skill_count:
            skill_count[sk]+=1
        else:
            skill_count[sk]=1
print(skill_count)

