import serial
import time
serdev = '/dev/ttyACM0'
s = serial.Serial(serdev, 9600)

s.write(bytes("\r", 'UTF-8'))
time.sleep(1)

s.write(bytes("/LEDControl/run 0 0\r", 'UTF-8'))
time.sleep(1)

s.write(bytes("/LEDControl/run 0 1\r", 'UTF-8'))
time.sleep(1)

s.write(bytes("/LEDControl/run 3 0\r", 'UTF-8'))
time.sleep(1)

s.write(bytes("/LEDControl/run 3 1\r", 'UTF-8'))
time.sleep(1)

s.close()