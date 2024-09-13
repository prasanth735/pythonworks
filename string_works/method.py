'valid string'
"valid string"
""" valid
string"""

company="ABC"
print(company.casefold())
print(company.capitalize()) #convert first letter to upper case 

#method inside class>>> object.method

company="LUMINAR"
print(company.lower())

company="luminar"
print(company.upper())# convert all letters to upper case

company1="luminar123"
print(company1.isalpha())#check all alphabet
print(company1.isalnum())# to check the entire string contain only alphabet and numbers

comapny3="12345"
print(comapny3.isdigit()) # to check the string contain all numbers

aaa="a 1234 a"
print(aaa.strip("a")) #remove the specfied charecter from right or left or both end

print(aaa.lstrip("a"))#lstrip >> remove from left side
print(aaa.rstrip("a"))#rstrip >> remove from right side

abc="hello football cricket"
ab=abc.split()
print(ab)
