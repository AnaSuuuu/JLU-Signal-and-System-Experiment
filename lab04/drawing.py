import numpy as np
import matplotlib.pyplot as plt

# 生成周期方波函数
def square_wave(frequency, duration, sampling_rate, amplitude, offset):
 t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
 return amplitude * 0.5 * (1 + np.sign(np.sin(2 * np.pi * frequency * t))) + offset

# 定义参数
fs = 5 # 5 kHz
fs_high = 100 # 100 kHz
duration = 0.5 # 10 ms
increased_sampling_rate = 30 * fs_high # 增加采样率，取1000 kHz的100倍

# 生成f(t)和s(t)
f_t = square_wave(fs, duration, increased_sampling_rate, amplitude=2, offset=-1)
s_t = square_wave(fs_high, duration, increased_sampling_rate, amplitude=1, offset=0)

# 计算傅里叶变换
f_freq = np.fft.fft(f_t)
s_freq = np.fft.fft(s_t)

# 获取频率轴
freq_axis = np.fft.fftfreq(len(f_t), 1/increased_sampling_rate)

# 计算fs(t)的波形和频谱
fs_t = f_t * s_t
fs_freq = np.fft.fft(fs_t)

# 获取单边频谱的索引
# positive_freq_index = np.where(freq_axis > 0)

# 绘制图形
plt.figure(figsize=(12, 8))

# 绘制f(t)的波形
plt.subplot(3, 2, 1)
plt.plot(np.linspace(0, duration, len(f_t), endpoint=False), f_t)
plt.title('Waveform of f(t)')

# 绘制f(t)的幅度谱
plt.subplot(3, 2, 2)
plt.plot(freq_axis, np.abs(f_freq))
# plt.plot(freq_axis[positive_freq_index], np.abs(f_freq[positive_freq_index]))
plt.title('Amplitude Spectrum of f(t)')

# 绘制s(t)的波形
plt.subplot(3, 2, 3)
plt.plot(np.linspace(0, duration, len(s_t), endpoint=False), s_t)
plt.title('Waveform of s(t)')

# 绘制s(t)的幅度谱
plt.subplot(3, 2, 4)
plt.xlim(-200, 200)
plt.plot(freq_axis, np.abs(s_freq))
# plt.plot(freq_axis[positive_freq_index], np.abs(s_freq[positive_freq_index]))
plt.title('Amplitude Spectrum of s(t)')

# 绘制fs(t)的波形
plt.subplot(3, 2, 5)
plt.plot(np.linspace(0, duration, len(fs_t), endpoint=False), fs_t)
plt.title('Waveform of fs(t)')

# 绘制fs(t)的幅度谱
plt.subplot(3, 2, 6)
plt.plot(freq_axis, np.abs(fs_freq))
# plt.plot(freq_axis[positive_freq_index], np.abs(fs_freq[positive_freq_index]))
plt.title('Amplitude Spectrum of fs(t)')

plt.tight_layout()
plt.show()