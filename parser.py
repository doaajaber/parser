

# important notes
  #1) make txt file in E directory naming it (input to parser)




token = "kk"   # dah global variable

def Error():            # al function dy al mfrood tw2f al brnamg w ttl3 error message
    print("Error")


def read():
    print("read")
def IF():
    print("if")
def exp():              # al function dy al mfrood thandle al exp
    print("exp")
def repeat():
    print("repeat")
def write():
    print("write")


def match(t):
    if t == token:
        token = next_token()
    else:
        Error()



def next_token():        # this function is used to get the next token in the input to parser file
    t = f.readline()
    index = t.find(",")
    return t[:index]









if __name__ == '__main__':
    f = open("E:\input to parser.txt", "r")
    token=next_token()
    print(next_token())
    print(next_token())
    #read();
    #IF();
    #exp();
    #repeat();
    #write();







