import matplotlib.pyplot as plt

temps = []
with open('temperature_file.txt', 'r') as f:
    temps = f.read().splitlines()

times = [n for n in range(5, 5 * len(temps) + 5, 5)]

plt.plot(times, [float(temp) for temp in temps])
plt.show()
