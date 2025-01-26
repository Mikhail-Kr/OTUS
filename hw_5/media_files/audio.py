from hw_5.media_files.media import Media

class Audio(Media):
    def __init__(self, name, size, created_at, owner, path, quality):
        super().__init__(name, size, created_at, owner, path)
        self.quality = quality

    def get_info(self):
        base_info = super().get_info()
        print(f'{base_info}. Quality: {self.quality}')