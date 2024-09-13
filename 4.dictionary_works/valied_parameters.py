user_input="{}()"

bracket_pairs={
    "{":"}",
    "(":")",
    "[":"]",
    "<":">"
}

symbol_stack=[]
top=-1

for symbol in user_input:
    if symbol in bracket_pairs:
        top+=1
        symbol_stack.append(symbol)
    else:
        if top==-1:
            print("invalid")
            break
        else:
            current_symbol=symbol_stack[top]
            current_symbol_closing=bracket_pairs.get(current_symbol)
            if current_symbol_closing==symbol:
                symbol_stack.pop()
                top-=1
            else:
                print("invalid")
                break
else:
    if len(symbol_stack)==0:
        print("valid")
    else:
        print("invalid")

