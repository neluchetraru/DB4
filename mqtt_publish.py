from read_temp import read_temp, init_temp_sensor
from umqtt.robust import MQTTClient
import os
import gc
import sys

# create a random MQTT clientID

# connect to Adafruit IO MQTT broker using unsecure TCP (port 1883)
#
# To use a secure connection (encrypted) with TLS:
#   set MQTTClient initializer parameter to "ssl=True"
#   Caveat: a secure connection uses about 9k bytes of the heap
#         (about 1/4 of the micropython heap on the ESP8266 platform)

try:
    client.connect()
except Exception as e:
    print('could not connect to MQTT server {}{}'.format(type(e).__name__, e))
    sys.exit()

ADAFRUIT_IO_FEEDNAME = b'DB4'


def connect():
    ADAFRUIT_IO_URL = b'io.adafruit.com'
    ADAFRUIT_USERNAME = b'chetraru_ion'
    ADAFRUIT_IO_KEY = b'aio_clNS70PuBy9vYl7XdUljW7JcLyw4'
    client = MQTTClient(client_id=mqtt_client_id,
                        server=ADAFRUIT_IO_URL,
                        user=ADAFRUIT_USERNAME,
                        password=ADAFRUIT_IO_KEY,
                        ssl=False)

    return client


# publish free heap statistics to Adafruit IO using MQTT
#
# format of feed name:
#   "ADAFRUIT_USERNAME/feeds/ADAFRUIT_IO_FEEDNAME"
mqtt_feedname = bytes(
    '{:s}/feeds/{:s}'.format(ADAFRUIT_USERNAME, ADAFRUIT_IO_FEEDNAME), 'utf-8')


def publish(feed):

    client.publish(feed, bytes(str(-1), 'utf-8'), qos=0)
