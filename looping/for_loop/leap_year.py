starting_year=1800
current_year=2024
for year in range(starting_year,current_year,1):
    if  year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        print(year)