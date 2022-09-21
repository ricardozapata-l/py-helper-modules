# ====================================================================================================
# Set of functions to handle external files & general system level operations
#
# Developed by @Zapata: rl-zapata.github.io
# ====================================================================================================
import os

# ¡--- General file operations ---!
# <--- Check if a directory exists if no create it --->
def createDirectory(directory_path):
    if not os.path.isdir(directory_path):
        os.makedirs(directory_path)

# <--- Save a file to a given location --->
def saveFile(file_object, file_path, file_name, file_extension):
    createDirectory(file_path)

    file_path_full = os.path.join(file_path, f'{file_name}.{file_extension}')
    file_object.save(file_path_full)

# <--- Open a file with the default system app --->
def openFile(file_path):
    import platform
    os_type = platform.system()

    if os_type == 'Linux':
        os.system(f'xdg-open "{file_path}"')
    elif os_type == 'Darwin':
        os.system(f'open "{file_path}"')
    elif os_type == 'Windows':
        os.startfile(file_path)
    else:
        print('Unknown OS \U0001F937')


# ¡--- Specific file operations ---!
# <--- Read an external SQL file --->
def readSQL(sql_path):
    with open(sql_path, 'r') as sql_query:
        sql_lines = sql_query.readlines()
    sql_query = ' '.join(line.strip() for line in sql_lines)

    return sql_query

# <--- Read an external JSON file --->
def readJSON(json_path):
    import json

    with open(json_path, 'r') as json_file:
        json_object = json.load(json_file)
    
    return json_object

# <--- Read a generic file--->
def readFile(file_path):
    with open(file_path, 'r') as file:
        file_object = file.read()

    return file_object