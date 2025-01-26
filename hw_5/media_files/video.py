from hw_5.media_files.media import Media

class Video(Media):
    def __init__(self, name, size, created_at, owner, path, resolution):
        super().__init__(name, size, created_at, owner, path)
        self.resolution = resolution

    def get_info(self):
        base_info = super().get_info()
        print(f'{base_info}. Resolution: {self.resolution}')