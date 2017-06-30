#使用多線程連接一對一藍芽裝置 如要一對多就增加port即可
#使用serial模擬藍牙串手
import serial
import sys
import threading
class Rfcomm(object):
    def __init__(self):
        self.port0 = '/dev/rfcomm1'
    def rfcomm0_d(self,*data):
            ser = serial.Serial(self.port0,115200,timeout=2)
            cmd= (str(data).encode('utf-8'))
            ser.write(cmd)
            ser.flushInput()
            ser.close()
if __name__ == '__main__':
    A = 'a'
    Thread_1 = threading.Thread(target = self.rfcomm0_d, args = A)
