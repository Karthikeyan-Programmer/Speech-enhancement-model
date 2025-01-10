import numpy as np
from scipy.io import wavfile
import scipy.signal
import matplotlib.pyplot as plt
from pydub import AudioSegment
import os
def Preprocessing():
    input_file = "Input_speech.wav"
    output_dir = "outputs"
    output_file_filtered = os.path.join(output_dir, "remove_artifacts.wav")
    output_file_normalized = os.path.join(output_dir, "output_normalized.wav")
    cutoff_frequency = 400
    sample_rate, audio_data = wavfile.read(input_file)
    nyquist_frequency = 0.5 * sample_rate
    normal_cutoff = cutoff_frequency / nyquist_frequency
    b, a = scipy.signal.butter(4, normal_cutoff, btype='low', analog=False)
    filtered_audio = scipy.signal.filtfilt(b, a, audio_data)
    wavfile.write(output_file_filtered, sample_rate, np.int16(filtered_audio))
    plt.figure(figsize=(10, 6))
    plt.subplot(3, 1, 1)
    plt.title('Input Audio')
    plt.plot(audio_data, color='blue')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.subplot(3, 1, 2)
    plt.title('Remove Artifacts Audio')
    plt.plot(filtered_audio, color='green')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    def normalize_audio(input_file, output_file, target_dBFS=-20):
        audio = AudioSegment.from_wav(input_file)
        normalized_audio = audio.normalize(target_dBFS)
        normalized_audio.export(output_file, format="wav")
    normalize_audio(output_file_filtered, output_file_normalized)
    sample_rate_normalized, audio_data_normalized = wavfile.read(output_file_normalized)
    plt.subplot(3, 1, 3)
    plt.title('Normalized Audio')
    plt.plot(audio_data_normalized, color='red')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()
    start_time = 0  
    end_time = 5  
    filtered_audio = AudioSegment.from_wav(output_file_filtered)
    selected_segment = filtered_audio[start_time * 1000:end_time * 1000]  # Convert times to milliseconds
    selected_output_file = os.path.join(output_dir, "selected_segment.wav")
    selected_segment.export(selected_output_file, format="wav")
    sample_rate_segment, audio_data_segment = wavfile.read(selected_output_file)
    plt.figure(figsize=(10, 6))
    plt.title('Selected Segment')
    plt.plot(audio_data_segment, color='blue')
    plt.xlabel('Sample Index')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()
