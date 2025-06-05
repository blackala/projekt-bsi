def read_file(file):
    with open(file, 'r') as f:
        return f.read()
    
def write_file(file, data):
    with open(file, 'w') as f:
        f.write(data)   