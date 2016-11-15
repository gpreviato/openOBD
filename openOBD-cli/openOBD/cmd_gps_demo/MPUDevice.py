"""The MPU command."""

from mpu6050 import mpu6050
import sys
import time
import os

class MPUDevice():
    def __init__(self):
        self.temperature = None
        self.accel  = None
        self.gyro = None
        self.init = None

    def init(self):
        self.init = mpu6050(0x68)

    def IgetTemp(self):
        self.temperature = mpu6050.get_temp(self.init)

    def IgetGyro(self):
        self.gyro = mpu6050.get_gyro_data(self.init)

    def IgetAccel(self):
        self.accel = mpu6050.get_accel_data(self.init)

    def printTempStream(self):
        print("Temperature:", self.temperature)

    def printAccelStream(self):
        print("Accelerometer:", self.accel)

    def printGyroStream(self):
        print("Gyroscope:", self.gyro)


        

