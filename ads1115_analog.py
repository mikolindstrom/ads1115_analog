import logging
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
from kalliope.core.NeuronModule import NeuronModule, MissingParameterException, InvalidParameterException

logging.basicConfig()
logger = logging.getLogger("kalliope")

# Initialize the I2C interface
i2c = busio.I2C(board.SCL, board.SDA)
# Create an ADS1115 object
ads = ADS.ADS1115(i2c)

class Ads1115_analog(NeuronModule):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.readChannel = kwargs.get('readChannel', None)
        
        if self.readChannel is None:
            raise InvalidParameterException("analog channel must be provided")
        
        analog_value = self.get_analog()
        self.analogvalue(analog_value)
        time.sleep(0.2)
        self.cleanup()

    def get_analog(self):
        if self.readChannel == ADS.P0:
            channel0 = AnalogIn(ads, ADS.P0)
            analog_value = channel0.value
        if self.readChannel == ADS.P1:
            channel1 = AnalogIn(ads, ADS.P1)
            analog_value = channel1.value
        if self.readChannel == ADS.P0:
            channel2 = AnalogIn(ads, ADS.P2)
            analog_value = channel2.value
        if self.readChannel == ADS.P3:
            channel3 = AnalogIn(ads, ADS.P3)
            analog_value = channel3.value

        return analog_value

    def cleanup(self):
        GPIO.cleanup()

    def analogvalue(self, analog_value):
        message = f"The Analog Value is : {analog_value} "
        self.say(message)
        logger.info(message)
