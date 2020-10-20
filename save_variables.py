file_save_name = r"data.txt"

#Read Only (‘r’) : Open text file for reading. The handle is positioned at the beginning of the file. If the file does not exists, raises I/O error. This is also the default mode in which file is opened.
#Read and Write (‘r+’) : Open the file for reading and writing. The handle is positioned at the beginning of the file. Raises I/O error if the file does not exists.
#Write Only (‘w’) : Open the file for writing. For existing file, the data is truncated and over-written. The handle is positioned at the beginning of the file. Creates the file if the file does not exists.
#Write and Read (‘w+’) : Open the file for reading and writing. For existing file, data is truncated and over-written. The handle is positioned at the beginning of the file.
#Append Only (‘a’) : Open the file for writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.
#Append and Read (‘a+’) : Open the file for reading and writing. The file is created if it does not exist. The handle is positioned at the end of the file. The data being written will be inserted at the end, after the existing data.

def get_lines():
    global file_save_name
    lines = 0
    with open(file_save_name, 'r') as f:
        for line in f:
            lines += 1
    return lines

def saveString(variable_name, value):
    global file_save_name
    line_to_write = 0
    write = False

    text = open(file_save_name, "r")
    text_lines = text.readlines()

    for i in range(0, get_lines()):
        variable = text_lines[i].split(':')
        if variable[0] == variable_name:
            line_to_write = i
            text_lines[line_to_write] = variable_name + ":" + value + "\n"
            write = True

    if write == False:
        text_lines.append(variable_name + ":" + value + "\n")

    with open(file_save_name, "w") as save:
        save.writelines(text_lines)
        save.close()

def getString(variable_name, default_value=""):
    global file_save_name
    value_found = ""
    did_find = False
    with open(file_save_name, 'r') as f:
        for line in f:
            line = line.split(':')
            if line[0] == variable_name:
                value_found = ""
                for i in range(1, len(line)):
                    value_found += line[i]
                    if i < len(line) - 1:
                        value_found += ":"
                did_find = True

        if not did_find:
            value_found = default_value
    return value_found.rstrip()

def saveArray(variable_name, value):
    global file_save_name
    line_to_write = 0
    write = False

    save_string = ""

    for i in range(0, len(value)):
        save_string += str(value[i])
        if i < len(value) - 1:
            save_string += ","

    text = open(file_save_name, "r")
    text_lines = text.readlines()

    for i in range(0, get_lines()):
        variable = text_lines[i].split(':')
        if variable[0] == variable_name:
            line_to_write = i
            text_lines[line_to_write] = variable_name + ":" + save_string + "\n"
            write = True

    if write == False:
        text_lines.append(variable_name + ":" + save_string + "\n")

    with open(file_save_name, "w") as save:
        save.writelines(text_lines)
        save.close()

def getArray(variable_name, default_value=[]):
    global file_save_name
    value_found = ""
    array = []
    did_find = False
    with open(file_save_name, 'r') as f:
        for line in f:
            line = line.split(':')
            if line[0] == variable_name:
                value_found = line[1]
                value_found = value_found.split(',')
                for i in range(0,len(value_found)):
                    array.append(value_found[i])
                array[len(array) - 1] = array[len(array) - 1].rstrip()
                did_find = True

        if not did_find:
            array = default_value
    
    return array

def deleteVariable(variable_name):
    global file_save_name
    line_to_delete = 0
    found_variable = False

    text = open(file_save_name, "r")
    text_lines = text.readlines()

    for i in range(0, get_lines()):
        variable = text_lines[i].split(':')
        if variable[0] == variable_name:
            line_to_delete = i
            found_variable = True
    
    if found_variable:
        text_lines.remove(text_lines[line_to_delete])

    with open(file_save_name, "w") as save:
        save.writelines(text_lines)
        save.close()

def setSaveFileName(path="data.txt"):
    global file_save_name
    file_save_name = path
    fole = open(file_save_name, "a")
    fole.close()