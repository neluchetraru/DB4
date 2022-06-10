import matplotlib.pyplot as plt
temps = [19.30276, 19.1297, 19.04315, 19.1297, 18.9566, 19.04315, 18.9566, 18.61051, 18.61051, 18.69702, 18.87009, 18.9566, 18.87009, 19.1297, 18.87009, 18.9566, 18.78357, 18.78357,
         19.04315, 18.9566, 18.69702, 18.61051, 18.69702, 18.37973, 18.61051, 18.61051, 18.9566, 18.49512, 18.78357, 18.69702, 18.61051, 18.37973, 18.61051, 18.17777, 18.49512, 18.37973]
times = [i*5 for i in range(36)]

plt.plot(times, temps)
plt.plot(times, [18]*len(times))
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.show()