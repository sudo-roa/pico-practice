from lcd1602 import LCD
from machine import Pin
import utime
import math
bit_0 = Pin(16,Pin.OUT)
bit_1 = Pin(17,Pin.OUT)
bit_2 = Pin(18,Pin.OUT)
bit_3 = Pin(19,Pin.OUT)
max_range = 15
input_range = 10

lcd = LCD()
string = " Hello!\n"
lcd.message(string)
utime.sleep(1)
string = "RaspberryPiPico!"
lcd.message(string)
utime.sleep(1)
lcd.clear()
utime.sleep(1)
#bit_1.value(0)

if(input_range<=max_range):
    for i in range(input_range):
        if(i<=1):
            rem0=i%2
            rem1=0
            rem2=0
            rem3=0
        elif(i<=3 and i>1):
            rem0=i%2
            rem1=math.floor(i/2)%2
            rem2=0
            rem3=0
        elif(i<=7 and i>3):
            rem0=i%2
            rem1=math.floor(i/2)%2
            rem2=math.floor(math.floor(i/2)/2)%2
            rem3=0
        elif(i<=15 and i>7):
            rem0=i%2
            rem1=math.floor(i/2)%2
            rem2=math.floor(math.floor(i/2)/2)%2
            rem3=math.floor(math.floor(math.floor(i/2)/2)/2)%2
        
        bit_0.value(rem0)
        bit_1.value(rem1)
        bit_2.value(rem2)
        bit_3.value(rem3)
        lcd.message(str(i))
        utime.sleep(1)
    
lcd.clear()
bit_0.value(0)
bit_1.value(0)
bit_2.value(0)
bit_3.value(0)
