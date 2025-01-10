import numpy as np
import librosa
import soundfile as sf
import tensorflow as tf
from tensorflow.keras import layers, models
import noisereduce as nr
import os

def speech_enhancement():
    def create_dummy_dataset(num_samples=1000, sequence_length=8000):
        X = np.random.randn(num_samples, sequence_length)
        noise = 0.5 * np.random.randn(num_samples, sequence_length)
        clean_signal = X + noise
        return clean_signal, X
    def create_model():
        model = models.Sequential()
        model.add(layers.Input(shape=(8000,)))
        model.add(layers.Dense(256, activation='relu'))
        model.add(layers.Dense(256, activation='relu'))
        model.add(layers.Dense(8000, activation='linear'))
        return model
    clean_data, noisy_data = create_dummy_dataset()
    model = create_model()
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(clean_data, noisy_data, epochs=10, batch_size=32, verbose=1)
    model.save('speech_enhancement_model.h5')
    sample = noisy_data[0]
    enhanced_sample = model.predict(sample.reshape(1, -1))
    enhanced_sample = enhanced_sample.reshape(-1)
    sf.write('enhanced_audio.wav', enhanced_sample, 8000)
    noisy_audio, sample_rate = sf.read("Input_speech.wav")
    reduced_audio = nr.reduce_noise(y=noisy_audio, sr=sample_rate)
    snr = 10 * np.log10(np.mean(noisy_audio**2) / np.mean((noisy_audio - reduced_audio)**2))
    mse = np.mean((noisy_audio - reduced_audio)**2)
    sf.write('enhanced_audio.wav', reduced_audio, sample_rate)
    print(f"Signal-to-Noise Ratio (SNR): {snr} dB")
    print(f"Mean Squared Error (MSE): {mse}")

