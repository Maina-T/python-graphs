import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
import numpy as np

xpoints = np.array([0.001,0.01, 0.1, 1])
ypoints = np.array([70.80, 98.63, 112.30, 153.23])
x_y_spline = make_interp_spline(xpoints, ypoints, k=1)
x_ = np.linspace(xpoints.min(), xpoints.max(), 50)
y_ = x_y_spline(x_)

x2points = np.array([0.001, 0.01, 0.1, 1])
y2points = np.array([52.73, 70.31, 106.44, 139.16])
x_y_spline = make_interp_spline(x2points, y2points, k=1)
x2_ = np.linspace(x2points.min(), x2points.max(), 50)
y2_ = x_y_spline(x2_)


x3points = np.array([0.001, 0.01, 0.1, 1])
y3points = np.array([48.34, 63.96, 79.59, 110.35])
x_y_spline = make_interp_spline(x3points, y3points, k=1)
x3_ = np.linspace(x3points.min(), x3points.max(), 50)
y3_ = x_y_spline(x3_)


x4points = np.array([0.001,0.01, 0.1, 1])
y4points = np.array([33.69, 41.69, 58.11, 95.70])
x_y_spline = make_interp_spline(x4points, y4points, k=1)
x4_ = np.linspace(x4points.min(), x4points.max(), 500)
y4_ = x_y_spline(x4_)


plt.plot(x_, y_, label = "1050 °C")
plt.plot(x2_, y2_, label = "1100 °C")
plt.plot(x3_, y3_, label = "1150 °C")
plt.plot(x4_, y4_, label = "1200 °C")


plt.xlabel("Strain rate (S-1)")
plt.ylabel("True stress (MPa)")

plt.grid()

plt.legend()

# plt.title('lnε=ηlnδ+lnA')

plt.show()