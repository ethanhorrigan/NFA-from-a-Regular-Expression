# Ethan Horrigan
# G00350712
# Program to build a non-deterministic ﬁnite automaton (NFA) from a regular expression

# Shunting Yard Algorithm

def shunt(infix):
 """Converts an infix expression to a postfix expression
    using the Shunting-yard algorithm"""
    
    # Specials Dictionary
    specials = {'*': 50, '.': 40, '|': 30}

    # pofix & stack string (empty)
    pofix = ""
    stack = ""

    #loop infix string
    for c in infix:
        if c == '(':
            stack = stack + c
        elif c == ')':
            while stack[-1] != '(':
                pofix = pofix + stack[-1]
                stack = stack[:-1]
            stack = stack[:-1] 
        elif c in specials:
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                pofix = pofix + stack[-1]
                stack = stack[:-1]  
            stack = stack + c
        else:
            pofix = pofix + c

    while stack:
        pofix = pofix + stack[-1]
        stack = stack[:-1]  

    return pofix

print(shunt("(a.b)|(c*.d)"))