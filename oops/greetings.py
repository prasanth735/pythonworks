#15/12/2023



def hello(fn):
    def wrapper(user):
        return "hello "+ fn(user)
    return wrapper

@hello
def morning_greeting(user):
    return f"good morning {user}"

@hello
def afternoon_greeting(user):
    return f"goodafter noon {user}"

def evening_greeting(user):

    return f"goodevening {user}"



# print(morning_greeting("hari"))

# print(afternoon_greeting("ameen"))

# print(evening_greeting("dev"))




def get_b(fn):
    def wrapper():
        return "<b> " +fn() + " <b>"
    return wrapper


@get_b
def get_hello():
    return "hello"

@get_b
def get_hai():
    return "hai"



print(get_hai())
print(get_hello())

