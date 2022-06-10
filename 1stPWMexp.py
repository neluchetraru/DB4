import matplotlib.pyplot as plt
temps = [18.37973, 17.7449, 18.00467, 18.00467, 18.00467, 17.83148, 17.65833, 18.09122, 18.26434, 18.17777, 17.91809, 18.49512, 18.17777, 18.37973, 18.26434, 18.09122, 18.09122, 18.17777,
         18.17777, 18.17777, 18.17777, 18.17777, 18.37973, 17.91809, 18.00467, 17.91809, 18.61051, 18.26434, 18.00467, 18.09122, 18.09122, 17.91809, 17.83148, 18.09122, 17.7449, 17.7449]
times = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90,
         95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175]

# We used P=4 for PID

plt.plot(times, temps)
plt.plot(times, [18]*len(times))
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.show()
