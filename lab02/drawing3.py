import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
  
font2 = {'color':'black','size':20} 

# 两个是配置代码，第一行表示，允许使用中文，第二个表示允许使用负数
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
 
# 这三个表示就跟名字一样，标识作用
plt.title("频谱图", fontdict=font2)
plt.xlabel("角频率ω", fontdict=font2, loc = "right")
plt.ylabel("谐波电压Un", fontdict=font2, loc = "top")
 
# 这个前两参数表示横坐标的开始和结尾，第三个参数表示你要分成多少份
x = np.linspace(0, 200, 10000)
y = np.linspace(0, 1, 100)
 
# 下面是节点个状态信息，一定要使用numpy自带的array，不然会出错
node1State = np.array([0.30, 0.28, 0.25, 0.22, 0.19, 0.15, 0.11, 0.07, 0.04, 0.01, 0.014, 0.02, 0.05, 0.06, 0.06, 0.05, 0.04, 0.03, 0.009, 0.006])
times = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])
 
# 这个就是最重要的平滑操作了，要是不使用这个操作的话，画出来的就是点和点之间的直线
model0 = make_interp_spline(times, node1State)
ys0 = model0(x)
 
# 给每条线设定颜色，和添加label，linestyle表示你要使用曲线的样式，有多少种网上有
plt.plot(x, ys0, linestyle='-.')#

 
# 给定点的横纵坐标
x_points = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
y_points = [0.30, 0.28, 0.25, 0.22, 0.19, 0.15, 0.11, 0.07, 0.04, 0.01, 0.014, 0.02, 0.05, 0.06, 0.06, 0.05, 0.04, 0.03, 0.009, 0.006]
plt.scatter(x_points, y_points, color='#1579ef')
# 创建垂线的长度
line_lengths =[0.30, 0.28, 0.25, 0.22, 0.19, 0.15, 0.11, 0.07, 0.04, 0.01, 0.014, 0.02, 0.05, 0.06, 0.06, 0.05, 0.04, 0.03, 0.009, 0.006]


# plt.scatter(x_points, y_points, label='给定点', color='blue')

# for i in range(len(x_points)):
#    plt.vlines(x = x_points[i], ymin = 0, ymax = line_lengths[i], color='red', linestyle='--')

x0 = np.arange(0, 200, 0.1)
y0 = abs(40 / (x0 * np.pi) * np.sin(x0 * np.pi / 100))
# plt.plot(x0,y0)

# legend() 函数只有在你需要使用laber 这个参数的时候才会用到
plt.legend()
plt.grid()
plt.show()
