
all_std_path=open("C:\\Users\\user\\Desktop\\my python\\fileio\\students.txt","r")

failed_path=open("C:\\Users\\user\\Desktop\\my python\\fileio\\failed.txt","r")

all_students_set=set()

failed_student_set=set()

for std in  all_std_path:
    student=std.rstrip("\n")
    all_students_set.add(student)
for std in failed_path:
    student=std.rstrip("\n")
    failed_student_set.add(student)


pass_student=all_students_set.difference(failed_student_set)
print(pass_student)