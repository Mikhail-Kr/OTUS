class Media:
    def __init__(self, name, size, created_at, owner, path):
        self.name = name
        self.size = size
        self.created_at = created_at
        self.owner = owner
        self.path = path

    def create(self):
        print(f'File with name {self.name} has been created.')

    def update(self):
        print(f'File with name {self.name} has been updated. Size: {self.size}')

    def delete(self):
        print(f'File with name {self.name} has been deleted.')

    def get_info(self):
        return f'File name is {self.name}. Size: {self.size}. Created: {self.created_at}. Owner: {self.owner}. Path: {self.path}'

    def download(self):
        print(f'File with name {self.name} has been downloaded from path: {self.path}')