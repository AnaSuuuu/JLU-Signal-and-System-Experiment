import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
 
font2 = {'color':'black','size':20} 

# 两个是配置代码，第一行表示，允许使用中文，第二个表示允许使用负数
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
 
# 这三个表示就跟名字一样，标识作用
plt.title("频谱图", fontdict=font2)
plt.xlabel("频率f", fontdict=font2, loc = "right")
plt.ylabel("幅频Nd(ω)", fontdict=font2, loc = "top")
 
# 这个前两参数表示横坐标的开始和结尾，第三个参数表示你要分成多少份
x = np.linspace(0, 45, 10000)
# y = np.linspace(0, 1, 100)
 
# 下面是节点个状态信息，一定要使用numpy自带的array，不然会出错
node1State = np.array([0.881048873, 0.794328235, 0.691830971, 0.595662144, 0.530884444, 0.45708819, 0.489778819, 0.375837404, 0.28840315])
times = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45])
 
# 这个就是最重要的平滑操作了，要是不使用这个操作的话，画出来的就是点和点之间的直线
model0 = make_interp_spline(times, node1State)
ys0 = model0(x)
 
# 给每条线设定颜色，和添加label，linestyle表示你要使用曲线的样式，有多少种网上有
plt.plot(x, ys0 , linestyle='-.')#
 
# 给定点的横纵坐标
x_points = [5, 10, 15, 20, 25, 30, 35, 40, 45]
y_points = [0.881048873, 0.794328235, 0.691830971, 0.595662144, 0.530884444, 0.45708819, 0.489778819, 0.375837404, 0.28840315]

# 创建垂线的长度
line_lengths = [0.57, 0.45, 0.30, 0.14, 0.03, 0.08, 0.13, 0.11, 0.09, 0.01]

plt.scatter(x_points, y_points, color='#1579ef')
# 画垂线
# for i in range(len(x_points)):
#    plt.vlines(x = x_points[i], ymin = 0, ymax = line_lengths[i], color='red', linestyle='--')

# 理想情况
x0 = np.arange(0, 45, 0.1)
y0 = 300 / np.sqrt(300 * 300 + np.pi * np.pi * x0 * x0 * 6.8 * 6.8 )
# y0 = abs(80 / (x0 * np.pi) * np.sin(x0 * np.pi / 100))
plt.plot(x0,y0)
# 300/SQRT(300*300+PI()*PI()*A1*A1*6.8*6.8/1000000)

# legend() 函数只有在你需要使用laber 这个参数的时候才会用到
plt.legend()
plt.grid()
plt.show()
