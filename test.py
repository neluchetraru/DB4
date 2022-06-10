from machine import I2C, Pin
import ssd1306
import machine
import time
from read_temp import read_temp
from read_temp import init_temp_sensor

import _thread
cooler = machine.Pin(14, machine.Pin.OUT)


motor_step_1 = machine.Pin(15, machine.Pin.OUT)
motor_dir_1 = machine.Pin(12, machine.Pin.OUT)  # change later the pin
motor_dir_1.value(1)
motor_step_2 = machine.Pin(33, machine.Pin.OUT)
motor_dir_2 = machine.Pin(27, machine.Pin.OUT)
motor_dir_2.value(1)


# def thread_function():
#     while True:
#         motor_step_1.value(not motor_step_2.value())
#         motor_step_2.value(not motor_step_2.value())
while True:
    motor_step_1.value(not motor_step_2.value())
    motor_step_2.value(not motor_step_2.value())

# # rev = 3200
# # for i in range(40*rev):
# _thread.start_new_thread(thread_function, ())

# temp = read_temp(init_temp_sensor(32))
# while True:
#     temp = read_temp(init_temp_sensor(32))
#     print(temp)
#     if temp > 18:
#         cooler.value(0)
#     else:
#         cooler.value(1)
#     time.sleep(0.5)


# def motor1():
#     while True:
#         motor_step_1.value(not motor_step_1.value())


# def motor2():
#     while True:
#         motor_step_2.value(not motor_step_2.value())


# _thread.start_new_thread(motor1, ())
# _thread.start_new_thread(motor2, ())

# Screen

# i2c = I2C(scl=Pin(22), sda=Pin(23), freq=100000)
# oled = ssd1306.SSD1306_I2C(128, 32, i2c)
# oled.fill(0)
# oled.text("Hi group 1!", 0, 8)
# oled.show()
