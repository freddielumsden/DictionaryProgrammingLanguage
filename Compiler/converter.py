def getConventions(file):
    file_line_number = 0
    file_line = file[file_line_number]
    conventions = []
    while file_line[0][0:10] == "convention":
        conventions += file_line[10:-2]
        file_line_number += 1
        file_line = file_line[file_line_number]
    return conventions, file_line_number


def getMainPos(file, ignore_up_to):
    file_line_number = ignore_up_to
    file_line = file[file_line_number]
    main_exists = False
    while file_line_number != len(file) - 1:
        file_line_number += 1
        file_line = file[file_line_number]
        if file_line[0][0:4] == "main":
            start = file_line_number
            main_exists = True
            break
    if main_exists:
        while file_line[0][0:1] == '\t':
            file_line_number += 1
            file_line = file[file_line_number]
        end = file_line_number
        return (start, end)


def converter(file):
    get_conventions = getConventions(file)
    conventions = get_conventions[0]
    ignore_up_to = get_conventions[1]
    keywords = {"main", "for", "if", "elif",
                "else", "while", "using", "convention"}
    main_vars = {}
    main_var_positions = {}
    main_pos = getMainPos(file, ignore_up_to)
    main_start = main_pos[0]
    main_end = main_pos[1]
    main = ""
    for line in file[main_start:main_end+3]:
        for word in line:
            main += word
        main += "\n"
    return main
