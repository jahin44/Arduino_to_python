import serial
import time

ser = serial.Serial('COM4', 9600,timeout=1)
time.sleep(2)

while(1):
    val=input("enter value")
    ser.write(val.encode('utf-8'))
    if val=='1':
        print("on")
    elif val=='0':
        print("off")
    else:
        print("number")




