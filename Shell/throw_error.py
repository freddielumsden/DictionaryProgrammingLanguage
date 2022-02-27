global error_thrown
error_thrown = False

def error(error_message, pos=None):
    if pos != None:
        for i in range(pos+4):
            print(end=' ')
        print('^')
    print("Error:", error_message)
    error_thrown = True
