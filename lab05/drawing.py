import numpy as np
import matplotlib.pyplot as plt

# 基本频率
f = 5
# 时间数组
t = np.linspace(0, 1, 500, endpoint=False)
# 生成锯齿波
y = signal.sawtooth(2 * np.pi * f * t)
# 以2f的频率采样
t_sample = np.arange(0, 1, 1/(2*f))
y_sample = signal.sawtooth(2 * np.pi * f * t_sample)

plt.figure()
plt.plot(t, y)
plt.stem(t_sample, y_sample, linefmt='r-', markerfmt='ro')
plt.show()
