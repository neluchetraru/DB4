import time
import network
from umqtt.robust import MQTTClient
import os
import sys


class MQTT:

    def __init__(self):
        random_num = int.from_bytes(os.urandom(3), 'little')
        self.mqtt_client_id = bytes('client_'+str(random_num), 'utf-8')
        self.ADAFRUIT_IO_URL = b'io.adafruit.com'
        self.ADAFRUIT_USERNAME = b'chetraru_ion'
        self.ADAFRUIT_IO_KEY = b'aio_clNS70PuBy9vYl7XdUljW7JcLyw4'

    def connectWIFI(self):
        WIFI_SSID = "Juan's network"
        WIFI_PASSWORD = 'qbjh0599'

        # turn off the WiFi Access Point
        ap_if = network.WLAN(network.AP_IF)
        ap_if.active(False)

        # connect the device to the WiFi network
        self.wifi = network.WLAN(network.STA_IF)
        self.wifi.active(True)
        self.wifi.connect(WIFI_SSID, WIFI_PASSWORD)

        # wait until the device is connected to the WiFi network
        MAX_ATTEMPTS = 20
        attempt_count = 0
        while not self.wifi.isconnected() and attempt_count < MAX_ATTEMPTS:
            attempt_count += 1
            time.sleep(1)

        if attempt_count == MAX_ATTEMPTS:
            print('Could not connect to the WiFi network')
            print('Continuing offline')

    def connectMQTT(self):
        client = MQTTClient(client_id=self.mqtt_client_id,
                            server=self.ADAFRUIT_IO_URL,
                            user=self.ADAFRUIT_USERNAME,
                            password=self.ADAFRUIT_IO_KEY,
                            ssl=False)
        self.client = client
        try:
            self.client.connect()
        except Exception as e:
            print('Could not connect to MQTT server {}{}'.format(
                type(e).__name__, e))
            sys.exit()

    def publish(self, feed, value):
        if not self.wifi.isconnected():
            print("No internet connection. Working offline.")
            return -1
        else:
            mqtt_feedname = bytes(
                '{:s}/feeds/{:s}'.format(self.ADAFRUIT_USERNAME, feed), 'utf-8')
            self.client.publish(mqtt_feedname, bytes(
                str(value), 'utf-8'), qos=0)
            return 0

    def subscribeTemp(self, PIDControl):
        def cbTemp(_, newTemp):
            print("New temperature change registered: " + str(newTemp, 'utf-8'))
            PIDControl.updateTemp(int(str(newTemp, 'utf-8')))
        if not self.wifi.isconnected():
            print("No internet connection. Working offline.")
        else:
            mqtt_feedname = bytes('chetraru_ion/feeds/desiredtemp', 'utf-8')
            self.client.set_callback(cbTemp)
            self.client.subscribe(mqtt_feedname)
