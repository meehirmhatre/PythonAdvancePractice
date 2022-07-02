# *argrs and **kwargs tutorials
# *vars and **kvars tutorial

def function_1(name, age, rollno):
    print("name ",name,"age ",age,"rollno ",rollno)

def function_2(*args):
    print(type(args))
    if(len(args)==3):
        print("name",args[0],"\nage",args[1],"\nrollno",args[2])
    else:
        print("name", args[0], "\nage", args[1])

def printmarks(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key,value)

# function_2("meehir",21)
#
# lis = ["hello",22,487498]
# function_2(*lis)

marklist = {"meehir" : 101, "meehir2" : 145,"meehir3" : 300,"manas":200}

printmarks(**marklist)
