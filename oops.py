class FileSystemObject:
    def __init__(self, name):
        self.name = name

class File(FileSystemObject):
    def __init__(self, name, content):
        super().__init__(name)
        self.content = content

class Directory(FileSystemObject):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def list_contents(self):
        print(f"Contents of directory '{self.name}':")
        for child in self.children:
            if isinstance(child, Directory):
                print(f"Directory: {child.name}")
            elif isinstance(child, File):
                print(f"File: {child.name}")

root = Directory("root")
docs = Directory("docs")
code = Directory("code")
file1 = File("readme.txt", "This is the readme file.")
file2 = File("script.py", "print('Hello, World!')")

root.add_child(docs)
root.add_child(code)
docs.add_child(file1)
code.add_child(file2)

root.list_contents()
