import cv2 as cv
import sys
import img_common as cm
import ast
import default_parameters as dp
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.signal as signal

if __name__ == '__main__':
    fs = 10000e3  # 采样率为100kHz
    T = 3 / 5e3  # 总时间为3个周期

    # 生成时间向量
    t = np.linspace(0, T, int(T * fs), endpoint=False)

    # 生成方波信号
    square_wave_5kHz = signal.square(2 * np.pi * 5e3 * t, duty=0.5)
    square_wave_100kHz = signal.square(2 * np.pi * 100e3 * t, duty=0.3)
    result_100kHz_upper = np.where(square_wave_100kHz >= 0, square_wave_100kHz, 0)

    # 绘制方波
    plt.plot(t, square_wave_5kHz)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('5kHz Square Wave')
    plt.grid(True)
    plt.show()

    t = np.linspace(0, T, int(T * fs), endpoint=False)

    # 生成方波信号
    result_100kHz_upper = np.where(square_wave_100kHz >= 0, square_wave_100kHz, 0)

    # 绘制方波
    plt.plot(t, result_100kHz_upper)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('100kHz Square Wave')
    plt.grid(True)
    plt.show()

    t = np.linspace(0, T, int(T * fs), endpoint=False)

    # 相乘得到新信号
    result = square_wave_5kHz * result_100kHz_upper

    # 绘制结果
    plt.plot(t, result)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Multiplication of 5kHz and 100kHz Square Waves')
    plt.grid(True)
    plt.show()

    # 计算频谱
    freq = np.fft.fftfreq(len(t), 1 / fs)
    result_freq = np.fft.fft(result)

    # 绘制频域图像
    freq_range = 1e6  # 指定显示的频率范围
    plt.figure(figsize=(10, 6))

    # 绘制5kHz方波的频域图像
    plt.subplot(322)
    plt.plot(freq, np.abs(np.fft.fft(square_wave_5kHz)))
    plt.xlim(-freq_range, freq_range)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title('Frequency Spectrum of 5kHz Square Wave')
    plt.grid(True)

    # 绘制100kHz方波的频域图像
    plt.subplot(324)
    plt.plot(freq, np.abs(np.fft.fft(result_100kHz_upper)))
    plt.xlim(-freq_range, freq_range)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title('Frequency Spectrum of 100kHz Square Wave')
    plt.grid(True)

    # 绘制相乘后信号的频域图像
    plt.subplot(326)
    plt.plot(freq, np.abs(result_freq))
    plt.xlim(-freq_range, freq_range)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title('Frequency Spectrum of Multiplication Result')
    plt.grid(True)

    plt.tight_layout()
    plt.show()