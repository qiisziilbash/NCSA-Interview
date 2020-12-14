import numpy as np
from scipy import fftpack
from matplotlib import pyplot as plt

step = 0.05
frequency = 0.5
times = np.arange(0, 8, step)
wave = np.sin(2 * np.pi * frequency * times)
noise = np.random.randn(times.size)
noisy_wave = wave + 0.2 * noise

plt.plot(times, noisy_wave, label='Original')
plt.xlabel('time(sec)')
plt.ylabel('value')


wave_fft = fftpack.fft(noisy_wave)
wave_fft_amp = np.abs(wave_fft)
wave_fft_power = wave_fft_amp ** 2 
wave_fft_angle = np.angle(wave_fft)
frequencies = fftpack.fftfreq(noisy_wave.size, d=step)

# plt.plot(frequencies, wave_fft_amp)
# plt.xlabel('Frequencies (Hz)')
# plt.ylabel('Amplitude')

max_amp = np.max(wave_fft_amp)
dominant_frequency = frequencies[wave_fft_amp.argmax()]
print(dominant_frequency)

# de-noise
clean_wave_fft = wave_fft.copy()
clean_wave_fft[np.abs(clean_wave_fft) < max_amp] = 0
clean_wave = fftpack.ifft(clean_wave_fft)

plt.plot(times, clean_wave, label='Filtered')
plt.legend()
plt.show()