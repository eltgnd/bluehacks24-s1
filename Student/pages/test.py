import pydub
from pydub import AudioSegment

pydub.AudioSegment.ffmpeg = "/audios/rain.mp3"
sound = AudioSegment.from_mp3("rain.mp3")