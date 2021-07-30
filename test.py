import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0.000952,0.000909, 0.00087, 0.00083])
ypoints = np.array([-0.045, -0.39, -0.489, -0.879])
m, b = np.polyfit(xpoints, ypoints, 1) # m = slope b = intercept
# print('Intercept:', b)
# print('Slope:', m)
# x axis values
# x = [1,2,3]
# corresponding y axis values
# y = [2,4,1]

x2points = np.array([0.000952,0.000909, 0.00087, 0.00083])
y2points = np.array([0.39, -0.054, -0.168, -0.65])
m2, b2 = np.polyfit(x2points, y2points, 1)
# print('Intercept:', b)
# print('Slope:', m)



x3points = np.array([0.000952,0.000909, 0.00087, 0.00083])
y3points = np.array([0.58, 0.503, 0.102, -0.28])
m3, b3 = np.polyfit(x3points, y3points, 1)
# print('Intercept:', b)
# print('Slope:', m)



x4points = np.array([0.000952,0.000909, 0.00087, 0.00083])
y4points = np.array([1.12, 0.94, 0.558, 0.349])
m4, b4 = np.polyfit(x4points, y4points, 1)
# print('Intercept:', b)
# print('Slope:', m)
avg_slope = (m+m2+m3+m4)/4

print('Average slope:',avg_slope)

# plt.plot(xpoints, ypoints,label = "1050")
# plt.plot(x2points, y2points,label = "1100")

# plt.plot(x3points, y3points,label = "1150")

# plt.plot(x4points, y4points,label = "1200")

# plt.plot(x, m*x + b)
plt.plot(xpoints, m*xpoints + b,label = "0.001 Strain rate (s-1)")

plt.plot(x2points, m2*x2points + b2,label = "0.01 Strain rate (s-1)")

plt.plot(x3points, m3*x3points + b3,label = "0.1 Strain rate (s-1)")

plt.plot(x4points, m4*x4points + b4,label = "1.0 Strain rate (s-1)")


plt.xlabel("1/T(c-1)")
plt.ylabel("ln(sinh(αδ))")

plt.grid()

plt.legend()

plt.title('ln(sinh(αδ)) = Q(1/T) + lnA')

plt.show()