# try / except / finally
try:
    file = open("xyz.txt",'r')
except EOFError as e:
    print("eof error")
except IOError as e:
    print("IOError")
finally:
    print("this will be printed irrespective of occurrence"
          "")