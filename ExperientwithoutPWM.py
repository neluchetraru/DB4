import matplotlib.pyplot as plt

# No PID, full speed of the motor. Switch between 12V and 5V based on whether
# In this experiment beased on the grpah we want to start slowing down at a value around 19 since
# the tubes still contain cold (12v) water and it will go down to a valley (around 17)

temps = [20.42841, 19.99527, 20.16852, 20.16852, 19.64896, 19.21622, 18.9566,
         18.9566, 18.87009, 18.78357, 18.37973, 18.61051, 18.26434, 18.37973,
         18.37973, 18.49512, 18.26434, 18.26434, 18.26434, 17.91809, 18.17777,
         18.00467, 17.65833, 17.83148, 17.7449, 17.57175, 17.91809, 17.83148,
         17.91809, 17.65833, 18.09122, 18.00467, 18.00467, 18.09122, 18.09122, 17.91809]

times = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85,
         90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155,
         160, 165, 170, 175]

plt.plot(times, temps)
plt.plot(times, [18]*len(times))
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.show()

errs = [-2.428406, -1.99527, -2.168518, -2.168518, -1.648956, -1.216217, -0.956604, -0.956604, -0.8700867, -0.7835693, -0.3797302, -0.6105042, -0.2643433, -0.3797302, -0.3797302, -0.4951172, -0.2643433, -0.2643433, -
        0.2643433, 0.08190918, -0.1777649, -0.004669189, 0.3416748, 0.1685181, 0.2550964, 0.4282532, 0.08190918, 0.1685181, 0.08190918, 0.3416748, -0.09121704, -0.004669189, -0.004669189, -0.09121704, -0.09121704, 0.08190918]
p = 15
for i in errs:
    ut = i * p
    print(ut)
