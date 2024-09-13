



import re


def checkpassword(password):
    score=5
    if len(password)>=8:
        score-=1
    if re.search(r'[a-z]',password):
        score-=1
    if re.search(r'[A-Z]',password):
        score-=1
    if re.search(r'[0-9]',password):
        score-=1
    if re.search(r'[!@#$%^&*]',password):
        score-=1
    print(score)

# checkpassword("Password@123")