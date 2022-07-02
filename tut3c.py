# try / except / else/ finally
try:
    print("i willl try thios code and will thrrow exception")
except Exception as e:
    print("i will run only if try block fails")
else:
    print("i will run if there is no exception. use this to run code which should only execute if there is no exception.")
finally:
    print("this will print in every case")