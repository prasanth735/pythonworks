# path="C:\\Users\\user\\Desktop\\my python\\fileio\\year.txt"

# f=open(path,"w")

# f.write("hello")

#-------------------------------------------------------------------------------------------------------------------------
# path="C:\\Users\\user\\Desktop\\my python\\fileio\\colors.txt"

# f=open(path,"w")
# colors=["green","blue","red"]

# for c in colors:
#     f.write(c+"\n")

#---------------------------------------------------------------------------------------------------------------------------
# path="C:\\Users\\user\\Desktop\\my python\\fileio\\year.txt"

# f=open(path,"w")

# for i in range(1800,2025):
#     if i%100==0:
#         f.write(str(i)+"\n")

#----------------------------------------------------------------------------------------------------------------------------------

# write all year 1800 - 22024

# path="C:\\Users\\user\\Desktop\\my python\\fileio\\year.txt"

# f=open(path,"w")

# for i in range(1800,2025):
#     f.write(str(i)+"\n")

#-----------------------------------------------------------------------------------------------------------------------------------------

# read years from year.txt and write all leap years
# write all leap years to leap year.tex

read_path="C:\\Users\\user\\Desktop\\my python\\fileio\\year.txt"
write_path="C:\\Users\\user\\Desktop\\my python\\fileio\\leap_year.txt"

fr=open(read_path,"r")
fw=open(write_path,"w")

for line in fr:
    year=int(line.rstrip("\n"))
    if year%100==0 and year%400==0 or year % 100!=0 and year%4==0:
        fw.write(str(year)+"\n")
