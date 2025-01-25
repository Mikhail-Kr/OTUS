from datetime import datetime

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

class Photo(Media):
    def __init__(self, name, size, created_at, owner, path, resolution):
        super().__init__(name, size, created_at, owner, path)
        self.resolution = resolution

    def get_info(self):
        base_info = super().get_info()
        print(f'{base_info}. Resolution: {self.resolution}')

class Audio(Media):
    def __init__(self, name, size, created_at, owner, path, quality):
        super().__init__(name, size, created_at, owner, path)
        self.quality = quality

    def get_info(self):
        base_info = super().get_info()
        print(f'{base_info}. Quality: {self.quality}')

class Video(Media):
    def __init__(self, name, size, created_at, owner, path, resolution):
        super().__init__(name, size, created_at, owner, path)
        self.resolution = resolution

    def get_info(self):
        base_info = super().get_info()
        print(f'{base_info}. Resolution: {self.resolution}')

class AudioS3(Audio):
    def __init__(self, name, size, created_at, owner, path, resolution, bucket):
        super().__init__(name, size, created_at, owner, path, resolution)
        self.bucket = bucket

    def download(self):
        print(f'File with name {self.name} has been downloaded from path: {self.path} and bucket: {self.bucket}')

photo = Photo('img', 1234, datetime.now(), 'im', 'localhost', '1920x1080')
photo.create()
photo.get_info()

audio = Audio('voice', 32452, datetime.now(), 'im', 'localhost', 'low')
audio.create()
audio.get_info()

video = Video('video', 32452, datetime.now(), 'im', 'localhost', '4k')
video.create()
video.get_info()

audio_s3 = AudioS3('voice1', 32452, datetime.now(), 'im', 's3_storage', '4k', 'garbage')
audio_s3.download()
audio.get_info()
