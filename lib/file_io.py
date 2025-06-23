
# lib/file_io.py

def write_file(file_name, file_content):
    file_path = f"{file_name}.txt"
    with open(file_path, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    file_path = f"{file_name}.txt"
    with open(file_path, 'a') as file:
        file.write(append_content)

def read_file(file_name):
    file_path = f"{file_name}.txt"
    with open(file_path, 'r') as file:
        return file.read()
