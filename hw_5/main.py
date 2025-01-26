from datetime import datetime

from hw_5.media_files.audio import Audio
from hw_5.media_files.photo import Photo
from hw_5.media_files.video import Video
from hw_5.cloud_storages.audio_s3 import AudioS3


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
