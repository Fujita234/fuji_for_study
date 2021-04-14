"""
y = 0.01x^2 + 0.1x の計算をした時のグラフです
数値微分の値を傾きとする直線のグラフを表示します

"""

import numpy as np
import matplotlib.pylab as plt

# 丸め誤差をした数値微分
def numerical_diff(f, x):
  h = 1e-4 # 0.0001
  return (f(x+h) - f(x-h)) / (2*h)

# y = 0.01x^2 + 0.1x の計算をしている。
# 本書での例で使われる式
def function_1(x):
  return 0.01*x**2 + 0.1*x 

# 接戦
def tangent_line(f, x):
  d = numerical_diff(f, x)
  print(d)
  y = f(x) - d*x
  return lambda t: d*t + y

x = np.arange(0.0, 20.0, 0.1) #0~20まで、0.1刻みのx配列
y = function_1(x) #それぞれを計算します
plt.xlabel("x")
plt.ylabel("f(x)")

tf = tangent_line(function_1, 5) 
y2 = tf(x)

plt.plot(x, y)
plt.plot(x, y2)
plt.show()
