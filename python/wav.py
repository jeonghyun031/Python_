#1
import wave

file = wave.open("6_input_audio.wav", 'rb')

print("Channels : ", file.getnchannels())

print("Width : ", file.getsampwidth())

print("original_frame_rate : ", file.getframerate())

print("num_frames : ", file.getnframes())

print("Duration : ", file.getnframes() / file.getframerate())
#2
import wave

import numpy as np

import scipy.signal as signal

input_file = '6_input_audio.wav'

new_sample_rate = 5000

with wave.open(input_file, 'rb') as wave_file:
    n_channels = wave_file.getnchannels()

    sample_width = wave_file.getsampwidth()

    sample_rate = wave_file.getframerate()

    n_frames = wave_file.getnframes()

    audio_data = wave_file.readframes(n_frames)

    audio_data = np.frombuffer(audio_data, dtype=np.int16)

    resampled_data = signal.resample(audio_data, int(len(audio_data) * float(new_sample_rate) / sample_rate))

output_file = 'resampled.wav'

with wave.open(output_file, 'wb') as wave_file:
    wave_file.setnchannels(n_channels)

    wave_file.setsampwidth(sample_width)

    wave_file.setframerate(new_sample_rate)

    wave_file.writeframes(resampled_data.tobytes())
#3
import wave

import numpy as np

import scipy.signal as signal

input_file = '6_input_audio.wav'

new_sample_rate = 11025

with wave.open(input_file, 'rb') as wave_file:
    n_channels = wave_file.getnchannels()

    sample_width = wave_file.getsampwidth()

    sample_rate = wave_file.getframerate()

    print("변경 전\nSample rate: ", sample_rate)

    n_frames = wave_file.getnframes()

    audio_data = wave_file.readframes(n_frames)

    audio_data = np.frombuffer(audio_data, dtype=np.int16)

    resampled_data = signal.resample(audio_data, int(len(audio_data) * float(new_sample_rate) / sample_rate))

output_file = 'resampled_2.wav'

with wave.open(output_file, 'wb') as wave_file:
    wave_file.setnchannels(n_channels)

    wave_file.setsampwidth(sample_width)

    wave_file.setframerate(new_sample_rate)

    wave_file.writeframes(resampled_data.tobytes())

file = wave.open("resampled_2.wav", 'rb')

print("변경 후\nSample rate: ", file.getframerate())