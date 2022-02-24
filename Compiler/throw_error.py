def error(error_message, line, file_split, pos=-1):
    print("Line", line+1, "- ", end='')
    print(error_message + ":")
    print(" ".join(file_split[line]))
    if pos != -1:
        if isinstance(pos, int):
            for i in range(pos):
                print(' ', end='')
            print("^")
        else:
            for i in range(pos[0]):
                print(' ', end='')
            for i in range(pos[1] - pos[0]):
                print('^', end='')
