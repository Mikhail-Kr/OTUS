from hw_5.media_files.audio import Audio

class AudioS3(Audio):
    def __init__(self, name, size, created_at, owner, path, resolution, bucket):
        super().__init__(name, size, created_at, owner, path, resolution)
        self.bucket = bucket

    def download(self):
        print(f'File with name {self.name} has been downloaded from path: {self.path} and bucket: {self.bucket}')