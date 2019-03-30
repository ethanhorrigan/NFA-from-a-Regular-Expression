# Ethan Horrigan
# G00350712
# Program to build a non-deterministic ﬁnite automaton (NFA) from a regular expression

# Shunting Yard Algorithm
def shunt(infix):


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


#State Class
class state:
    label = None
    edge1 = None
    edge2 = None

#Nfa Class
class nfa:
    initial = None
    accept = None

    #Constructor
    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept

def compile(postfix):
    nfastack = []

    for c in postfix:
        #Concatenate
        if c == '.':
            #Pop 2 nfas off the stack
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()

            #Connect nfa1 accept edge to nfa2 initial
            nfa1.accept.edge1 = nfa2.initial

            #Create new nfa and add back to the stack
            newNFA = nfa(nfa1.initial, nfa2.accept)
            nfastack.append(newNFA)
        #OR
        elif c == '|':
            #Pop 2 nfas off the stack
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()

            #Create 2 new states, 1 inital and 1 accept
            initial = state()
            accept = state()

            #Connect new initial to the each nfa initial
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial

            #Connect edge of nfa accept state to new accept state
            nfa1.accept.edge1 = accept
            nfa2.accept.edge1 = accept

            #Create new nfa and add back to the stack
            newNFA = nfa(initial, accept)
            nfastack.append(newNFA)
        #0 or many
        elif c == '*':
            #Pop one nfa off the stack
            nfa1 = nfastack.pop()

            #Create 2 new states, 1 inital and 1 accept
            initial = state()
            accept = state()

            #E arrows
            #Connect new initial to nfa1 inital
            initial.edge1 = nfa1.initial
            #Accept if string is empty
            initial.edge2 = accept

            #Connecting back to the initial state 
            nfa1.accept.edge1 = nfa1.initial
            #String is accepted
            nfa1.accept.edge2 = accept

            #Create new nfa and add back to the stack
            newNFA = nfa(initial, accept)
            nfastack.append(newNFA)
        #One or more
        elif c == '+':
            #Pop one nfa off the stack
            nfa1 = nfastack.pop()

            #Create 2 new states, 1 inital and 1 accept
            initial = state()
            accept = state()

            #E arrows
            #Connect new initial to nfa1 inital
            initial.edge1 = nfa1.initial

            #Connecting back to the initial state 
            nfa1.accept.edge1 = nfa1.initial
            #String is accepted
            nfa1.accept.edge2 = accept

            #Create new nfa and add back to the stack
            newNFA = nfa(initial, accept)
            nfastack.append(newNFA)
        #0 or 1
        elif c == '?':
            #Pop one nfa off the stack
            nfa1 = nfastack.pop()

            #Create 2 new states, 1 inital and 1 accept
            initial = state()
            accept = state()

            #E arrows
            #Accept if string is empty
            initial.edge2 = accept
            #Connect new initial to nfa1 inital
            initial.edge1 = nfa1.initial
            
            #String is accepted
            nfa1.accept.edge2 = accept

            #Create new nfa and add back to the stack
            newNFA = nfa(initial, accept)
            nfastack.append(newNFA)
        #Other Characters
        else: 
            
            #Create 2 new states, 1 inital and 1 accept
            accept = state()
            initial = state()

            #Initial label = character that is not one of the operators
            initial.label = c
            #Connect initial directly to the accept state
            initial.edge1 = accept

            #Create new nfa and add back to the stack
            newNFA = nfa(initial, accept)
            nfastack.append(newNFA)

    return nfastack.pop()


