import matplotlib.pyplot as plt
# P =
# temps1 = []

# with open('temperature_file.txt', 'r') as f:
#     temps1 = f.read().splitlines()
# times1 = [i for i in range(5, len(temps1) * 5 + 5, 5)]

# plt.plot(times1, [float(temp) for temp in temps1])
# plt.xlabel("Time")
# plt.ylabel("Temperature")
# plt.plot(times1, [19] * len(times1))
# plt.title("No PID Control")
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
plt.plot(times4, [float(temp) for temp in temps4])
plt.plot(times4, [19] * len(times4))
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("PID CONTROL" + "\n" + "5v when T < 19.5")
plt.show()

# u_ts4 = []
# with open('ut 1.txt', 'r') as f:
#     u_ts4 = f.read().splitlines()

# plt.plot(times4, [float(temp) for temp in temps4])
# plt.plot(times4, [19] * len(times4))

# plt.show()
# times4 = [i for i in range(0, len(temps4) * 5 + 5, 5)]
# plt.plot(times4, [float(u_t) for u_t in u_ts4])
# plt.show()


# temps5 = []

# with open('temp 1.txt', 'r') as f:
#     temps5 = f.read().splitlines()
# times5 = [i for i in range(5, len(temps5) * 5 + 5, 5)]

# u_ts5 = []
# with open('ut 1.txt', 'r') as f:
#     u_ts5 = f.read().splitlines()

# plt.plot(times5, [float(temp) for temp in temps5])
# plt.plot(times5, [19] * len(times5))

# plt.show()
# times5 = [i for i in range(0, len(temps5) * 5 + 5, 5)]
# plt.plot(times5, [float(u_t) for u_t in u_ts5])
# plt.show()


# temps6 = []

# with open('temp 2.txt', 'r') as f:
#     temps6 = f.read().splitlines()
# times6 = [i for i in range(5, len(temps6) * 5 + 5, 5)]
# plt.plot(times6, [float(temp) for temp in temps6])
# plt.plot(times6, [19] * len(times6))
# plt.show()

# temps7 = []

# with open('temp 53762142.txt', 'r') as f:
#     temps7 = f.read().splitlines()
# times7 = [i for i in range(5, len(temps7) * 5 + 5, 5)]
# plt.plot(times7, [float(temp) for temp in temps7])
# plt.plot(times7, [19] * len(times7))
# plt.show()


temps8 = []

with open('temp 35.txt', 'r') as f:
    temps8 = f.read().splitlines()
times8 = [i for i in range(5, len(temps8) * 5 + 5, 5)]
plt.plot(times8, [float(temp) for temp in temps8])
print([float(temp) for temp in temps8])
plt.plot(times8, [19] * len(times8))
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("PID CONTROL" + "\n" + "I = 0.5, P = 2, D = 0")
plt.show()


# temps9 = []

# with open('temp 38.txt', 'r') as f:
#     temps9 = f.read().splitlines()
# times9 = [i for i in range(5, len(temps9) * 5 + 5, 5)]
# plt.plot(times9, [float(temp) for temp in temps9])
# print([float(temp) for temp in temps9])
# plt.plot(times9, [19] * len(times9))
# plt.xlabel("Time")
# plt.ylabel("Temperature")
# plt.title("PID CONTROL" + "\n" + "I = 0.15, P = 2, D = 0")
# plt.show()
