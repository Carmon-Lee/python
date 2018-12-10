import json
import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt


def synthesizer(freq, duration, amp=1.0, sampling_freq=44100):
    t = np.linspace(0, duration, duration * sampling_freq)
    audio = amp * np.sin(2 * np.pi * freq * t)
    return audio.astype(np.int16)


if __name__ == '__main__':
    tone_map_file = 'tone_freq_map.json'
    with open(tone_map_file) as f:
        tone_freq_map = json.loads(f.read())

    input_tone = 'G1'
    duration = 2
    amplitude = 10000
    sampling_freq = 44100
    for i,j in tone_freq_map.items():
        synthesized_tone = synthesizer(tone_freq_map[i], duration, amplitude, sampling_freq)
        write('output'+i.replace('/','')+'.wav', sampling_freq, synthesized_tone)

