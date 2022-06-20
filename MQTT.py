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
        self.online = False

    def connectWIFI(self):
        WIFI_SSID = "Juan's network"
        WIFI_PASSWORD = 'qbjh0599'

        # turn off the WiFi Access Point
        ap_if = network.WLAN(network.AP_IF)
        ap_if.active(False)

        # connect the device to the WiFi network
        self.wifi = network.WLAN(network.STA_IF)
        self.wifi.active(True)
        if not self.wifi.isconnected():
            try:
                self.wifi.connect(WIFI_SSID, WIFI_PASSWORD)
            except:
                return False
        # wait until the device is connected to the WiFi network
            MAX_ATTEMPTS = 5
            attempt_count = 0
            while not self.wifi.isconnected() and attempt_count < MAX_ATTEMPTS:
                attempt_count += 1
                time.sleep(1)

            if attempt_count == MAX_ATTEMPTS:
                print('Could not connect to the WiFi network')
                print('Continuing offline')
                return False
        return True

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

    def connect(self):
        self.connectWIFI()
        if self.wifi.isconnected():
            self.connectMQTT()
            self.online = True
        else:
            self.online = False

    def publish(self, feed, value):
        if self.online:
            mqtt_feedname = bytes(
                '{:s}/feeds/{:s}'.format(self.ADAFRUIT_USERNAME, feed), 'utf-8')
            self.client.publish(mqtt_feedname, bytes(
                str(value), 'utf-8'), qos=0)

    def subscribeData(self, cb, feed):
        if self.online:
            mqtt_feedname = bytes(
                'chetraru_ion/feeds/{}'.format(feed), 'utf-8')
            self.client.set_callback(cb)
            self.client.subscribe(mqtt_feedname)
