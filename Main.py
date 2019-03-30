# Ethan Horrigan
# G00350712
# Program to build a non-deterministic ﬁnite automaton (NFA) from a regular expression

# Shunting Yard Algorithm
def shunt(infix):
    # Specials Dictionary with character and precedence
    specials = {'+': 70, '?': 60, '*': 50, '.': 40, '|':30}

    # Empty Pofix & Stack Strick
    pofix = ""
    stack = ""

    #loop infix string
    for c in infix:
        #If loop encounters open bracket, add to stack.
        if c == '(':
            stack = stack + c
        #If loop encounters closing bracket, take all off stack & add to postfix
        elif c == ')':
            while stack[-1] != '(':
                pofix = pofix + stack[-1]
                stack = stack[:-1]
            stack = stack[:-1] 
        #If loop encounters special character, check if a character in the stack has higher precedence, add it to postfix 
        elif c in specials:
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                pofix = pofix + stack[-1]
                stack = stack[:-1]  
            stack = stack + c
        #If loop encounters anything else, add to stack
        else:
            pofix = pofix + c

    while stack:
        pofix = pofix + stack[-1]
        stack = stack[:-1]  

    return pofix

# print(shunt("(a.b)|(c*.d)"))


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

            #Create 2 new states
            initial = state()
            accept = state()

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
            #Pop one NFA off the stack
            nfa1 = nfastack.pop()

            #Create 2 new states
            initial = state()
            accept = state()

            #Accept if string is empty
            initial.edge2 = accept
            #Connect new initial to nfa1 inital
            initial.edge1 = nfa1.initial
            
            #String is accepted
            nfa1.accept.edge2 = accept

            #Create new nfa and add to the stack
            newNFA = nfa(initial, accept)
            nfastack.append(newNFA)
        else: 
            
            #Create 2 new states
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

def followes(state):

    #Create new Set
    states = set()
    #Add state to states set
    states.add(state) 

    if state.label is None:
        # If the state has an edge 1 follow it
        if state.edge1 is not None:
            states |= followes(state.edge1)
        # If the state has an edge 2 follow it
        if state.edge2 is not None:
            states |= followes(state.edge2)

    return states

def match(opt,infix,string):
    if opt == 1:
        #Converts infix to postfix
        postfix = shunt(infix)
        #Creates an NFA from postfix 
        nfa = compile(postfix)
    elif opt == 2:
        #Sets infix to postfix variable
        postfix = infix
        #Creates an NFA from postfix 
        nfa = compile(postfix)

    current = set()
    next = set()

    current |= followes(nfa.initial)

    #Loop through characters in the string
    for s in string:
        #Loop through states
        for c in current:
            #Checks if c.label and s are equal 
            if c.label == s:
                #add to the next set of states
                next |= followes(c.edge1)

        #Setting current set of states to next state
        current = next
        #clear set for next character
        next = set()

    return (nfa.accept in current)

#Running boolean initialized to false (While false menu will continue to run)
running = False

#While Loop containing options for user input
while running != True:
    print("\nPlease Choose an Option:\n[1] Enter Infix \n[2] Enter Postfix \n[3] Exit\n")
    opt = input("Option: ")

    #User can enter a infix expression & a string     
    if opt == "1":
        infix = input("Enter Infix Expression:")
        stringi = input("Enter String:")
        print("\n")
        print(" Postfix: ",shunt(infix))
        print("",match(1,infix,stringi),"\n Infix:",infix,"\n String:",stringi)
        print("\n")
    #User can enter a postfix expression & a string      
    elif opt == "2":
        postfix = input("Enter Postfix Expression:")
        stringp = input("Enter String:")
        print("\n")
        print("",match(2,postfix,stringp),"\n Postfix:",postfix,"\n String:",stringp)
        print("\n")
    #Exit Program
    elif opt == "3":
        running = True
            
