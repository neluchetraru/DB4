import matplotlib.pyplot as plt


# P =
# temps1 = []

# with open('temperature_file.txt', 'r') as f:
#     temps1 = f.read().splitlines()
# times1 = [i for i in range(5, len(temps1) * 5 + 5, 5)]


# plt.plot(times1, [float(temp) for temp in temps1])
# plt.show()


# P = 2 D = 0.2 I = 0.5
# temps2 = []

# with open('temperature_file.txt', 'r') as f:
#     temps2 = f.read().splitlines()
# times2 = [i for i in range(5, len(temps2) * 5 + 5, 5)]
# with open('temperature_file.txt', 'r') as f:
#     temps2 = f.read().splitlines()
# times2 = [i for i in range(5, len(temps2) * 5 + 5, 5)]


# u_ts2 = []
# with open('ut_file.txt', 'r') as f:
#     u_ts2 = f.read().splitlines()

# plt.plot(times2, [float(temp) for temp in temps2])
# plt.plot(times2, [19] * len(times2))

# plt.show()
# times2 = [i for i in range(0, len(temps2) * 5 + 5, 5)]
# plt.plot(times2, [float(u_t) for u_t in u_ts2])
# plt.show()

# D = 0
# temps3 = []

# with open('temperature_file.txt', 'r') as f:
#     temps3 = f.read().splitlines()
# times3 = [i for i in range(5, len(temps3) * 5 + 5, 5)]

# u_ts3 = []
# with open('ut_file.txt', 'r') as f:
#     u_ts3 = f.read().splitlines()

# plt.plot(times3, [float(temp) for temp in temps3])
# plt.plot(times3, [19] * len(times3))

# plt.show()
# times3 = [i for i in range(0, len(temps3) * 5 + 5, 5)]
# plt.plot(times3, [float(u_t) for u_t in u_ts3])
# plt.show()

# we put 5 v when temp <=19.5
temps3 = []

with open('temp 1.txt', 'r') as f:
    temps4 = f.read().splitlines()
times4 = [i for i in range(5, len(temps4) * 5 + 5, 5)]

u_ts4 = []
with open('ut 1.txt', 'r') as f:
    u_ts4 = f.read().splitlines()

plt.plot(times4, [float(temp) for temp in temps4])
plt.plot(times4, [19] * len(times4))

plt.show()
times4 = [i for i in range(0, len(temps4) * 5 + 5, 5)]
plt.plot(times4, [float(u_t) for u_t in u_ts4])
plt.show()
