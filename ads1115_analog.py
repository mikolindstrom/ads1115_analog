import logging
import busio
import digitalio
import board
import microcontroller
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import time
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
        
        if self.readChannel == 'ADS.P0':
            channel0 = AnalogIn(ads, ADS.P0)
            analog_value = channel0.value
            message = f"The Analog Value is : {analog_value} "
            self.say(message)
            logger.info(message)
        if self.readChannel == 'ADS.P1':
            channel1 = AnalogIn(ads, ADS.P1)
            analog_value = channel1.value
            message = f"The Analog Value is : {analog_value} "
            self.say(message)
            logger.info(message)
        if self.readChannel == 'ADS.P2':
            channel2 = AnalogIn(ads, ADS.P2)
            analog_value = channel2.value
            message = f"The Analog Value is : {analog_value} "
            self.say(message)
            logger.info(message)
        if self.readChannel == 'ADS.P3':
            channel3 = AnalogIn(ads, ADS.P3)
            analog_value = channel3.value
            message = f"The Analog Value is : {analog_value} "
            self.say(message)
            logger.info(message)
        
        time.sleep(0.2)

