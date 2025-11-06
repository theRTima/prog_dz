class Files:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def write(self, content):
        with open(self.file_name, 'w') as f:
            f.write(content)
    
    def read(self):
        with open(self.file_name, 'r') as f:
            return f.read()
    
    def append_line(self, content):
        with open(self.file_name, 'a') as f:
            f.write(content)

file_test = Files("test.txt")
file_test.write("first one\n")
file_test.append_line("second one")
print(file_test.read())