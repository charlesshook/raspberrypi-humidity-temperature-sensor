import time
import board
import adafruit_sht31d

class SHT31:
    def __init__(self):
        i2c = board.I2C()
        self.sensor = adafruit_sht31d.SHT31D(i2c)

    def readAll(self):
        return self.sensor.temperature, self.sensor.relative_humidity
    
    def readTemperature(self):
        return self.sensor.temperature

    def readRelativeHumidity(self):
        return self.sensor.relative_humidity

    def heater(self, seconds):
        self.sensor.heater = True
        time.sleep(seconds)
        self.sensor.heater = False 
        
