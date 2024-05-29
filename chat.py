import pyopenjtalk
import numpy as np
from scipy.io import wavfile

text = "AI Academyで音声合成を学んでいます"
x, sr = pyopenjtalk.tts(text)
wavfile.write("output.wav", sr, x.astype(np.int16))
